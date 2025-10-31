// LANGUAGE: C
// ENV: GCC / Clang
// AUTHOR: Gabriel Rabelo
// GITHUB: https://github.com/gabrielrab

// Mini-Zip is a simple zip file compressor and decompressor.
// It is a single-file implementation of the zip file format.
// It is a simple implementation of the zip file format.
// It is a simple implementation of the zip file format.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

#define WINDOW_SIZE 4096
#define MIN_MATCH      3
#define MAX_MATCH    255
#define ESCAPE      0xFF
#define LIT_TAG     0x00
#define MATCH_TAG   0x01

typedef uint8_t  u8;
typedef uint16_t u16;

// Returns the size of the opened file without changing the current position.
static unsigned long file_size(FILE *f) {
    long cur = ftell(f);
    fseek(f, 0, SEEK_END);
    long sz = ftell(f);
    fseek(f, cur, SEEK_SET);
    return (unsigned long)sz;
}

// Reads the entire file into memory and returns its buffer and length.
static u8* read_all(const char *path, size_t *out_len) {
    FILE *f = fopen(path, "rb");
    if (!f) return NULL;
    unsigned long sz = file_size(f);
    u8 *buf = (u8*)malloc(sz ? sz : 1);
    if (!buf) { fclose(f); return NULL; }
    size_t n = fread(buf, 1, sz, f);
    fclose(f);
    *out_len = n;
    return buf;
}

// Writes the given buffer to disk; returns nonzero on success.
static int write_all(const char *path, const u8 *buf, size_t len) {
    FILE *f = fopen(path, "wb");
    if (!f) return 0;
    size_t n = fwrite(buf, 1, len, f);
    fclose(f);
    return n == len;
}

// Finds the longest backward match for position 'pos' within a sliding window.
static void find_longest_match(const u8 *in, size_t n, size_t pos,
                               size_t *best_off, size_t *best_len) {
    size_t start = (pos > WINDOW_SIZE) ? (pos - WINDOW_SIZE) : 0;
    size_t max_len = (n - pos > MAX_MATCH) ? MAX_MATCH : (n - pos);

    *best_off = 0;
    *best_len = 0;

    if (max_len < MIN_MATCH) return;

    for (size_t s = pos; s-- > start; ) {
        size_t L = 0;
        while (L < max_len && in[s + L] == in[pos + L]) {
            L++;
        }
        if (L >= MIN_MATCH && L > *best_len) {
            *best_len = L;
            *best_off = pos - s;
            if (L == max_len) break;
        }
    }
}

// Compresses input using a simple LZ77-like scheme; allocates and returns output.
static int compress_toy(const u8 *in, size_t n, u8 **out_buf, size_t *out_len) {
    size_t cap = n * 2 + 1024;
    u8 *out = (u8*)malloc(cap);
    if (!out) return 0;

    size_t i = 0, w = 0;

    while (i < n) {
        size_t off = 0, mlen = 0;
        find_longest_match(in, n, i, &off, &mlen);

        if (mlen >= MIN_MATCH) {
            if (w + 5 > cap) { cap *= 2; out = (u8*)realloc(out, cap); if(!out) return 0; }
            out[w++] = ESCAPE;
            out[w++] = MATCH_TAG;
            u16 o = (u16)off;
            out[w++] = (u8)((o >> 8) & 0xFF);
            out[w++] = (u8)(o & 0xFF);
            out[w++] = (u8)mlen;
            i += mlen;
        } else {
            u8 b = in[i++];
            if (b == ESCAPE) {
                if (w + 3 > cap) { cap *= 2; out = (u8*)realloc(out, cap); if(!out) return 0; }
                out[w++] = ESCAPE;
                out[w++] = LIT_TAG;
                out[w++] = ESCAPE;
            } else {
                if (w + 1 > cap) { cap *= 2; out = (u8*)realloc(out, cap); if(!out) return 0; }
                out[w++] = b;
            }
        }
    }

    *out_buf = out;
    *out_len = w;
    return 1;
}

// Decompresses data produced by compress_toy; allocates and returns output.
static int decompress_toy(const u8 *in, size_t n, u8 **out_buf, size_t *out_len) {
    size_t cap = n * 4 + 1024;
    u8 *out = (u8*)malloc(cap);
    if (!out) return 0;

    size_t r = 0, w = 0;

    while (r < n) {
        u8 b = in[r++];

        if (b != ESCAPE) {
            if (w + 1 > cap) { cap *= 2; out = (u8*)realloc(out, cap); if(!out) return 0; }
            out[w++] = b;
            continue;
        }

        if (r >= n) { free(out); return 0; }
        u8 tag = in[r++];

        if (tag == LIT_TAG) {
            if (r >= n) { free(out); return 0; }
            u8 lit = in[r++];
            if (w + 1 > cap) { cap *= 2; out = (u8*)realloc(out, cap); if(!out) return 0; }
            out[w++] = lit;
        } else if (tag == MATCH_TAG) {
            if (r + 3 > n) { free(out); return 0; }
            u16 off = ((u16)in[r] << 8) | in[r + 1];
            u8  len = in[r + 2];
            r += 3;

            if (off == 0 || len < MIN_MATCH) { free(out); return 0; }
            if (off > w) { free(out); return 0; }

            if (w + len > cap) {
                while (w + len > cap) cap *= 2;
                out = (u8*)realloc(out, cap);
                if(!out) return 0;
            }
            for (u16 k = 0; k < len; k++) {
                out[w] = out[w - off];
                w++;
            }
        } else {
            free(out);
            return 0;
        }
    }

    *out_buf = out;
    *out_len = w;
    return 1;
}

// Prints CLI usage instructions.
static void usage(const char *prog) {
    fprintf(stderr, "Uso:\n  %s c <input> <output>   # comprimir\n  %s d <input> <output>   # descomprimir\n", prog, prog);
}

// Entry point: routes to compression or decompression based on argv[1].
int main(int argc, char **argv) {
    if (argc != 4) { usage(argv[0]); return 1; }

    const char mode = argv[1][0];
    const char *in_path  = argv[2];
    const char *out_path = argv[3];

    size_t in_len = 0;
    u8 *in_buf = read_all(in_path, &in_len);
    if (!in_buf) {
        fprintf(stderr, "Erro ao ler: %s\n", in_path);
        return 1;
    }

    u8 *out_buf = NULL;
    size_t out_len = 0;
    int ok = 0;

    if (mode == 'c') {
        ok = compress_toy(in_buf, in_len, &out_buf, &out_len);
    } else if (mode == 'd') {
        ok = decompress_toy(in_buf, in_len, &out_buf, &out_len);
    } else {
        usage(argv[0]);
        free(in_buf);
        return 1;
    }

    if (!ok) {
        fprintf(stderr, "Falha no %s\n", (mode=='c'?"compressor":"descompressor"));
        free(in_buf);
        free(out_buf);
        return 1;
    }

    if (!write_all(out_path, out_buf, out_len)) {
        fprintf(stderr, "Erro ao escrever: %s\n", out_path);
        free(in_buf);
        free(out_buf);
        return 1;
    }

    fprintf(stderr, "%s OK: %zu bytes -> %zu bytes\n",
            (mode=='c'?"Comprimido":"Descomprimido"), in_len, out_len);

    free(in_buf);
    free(out_buf);
    return 0;
}
