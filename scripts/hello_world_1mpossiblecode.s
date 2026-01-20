// LANGUAGE: Assembly
// ENV: macosx + arm64
// AUTHOR: 1mpossible-code
// GITHUB: https://github.com/1mpossible-code
//
// To run: as -o hello_world_1mpossiblecode.o hello_world_1mpossiblecode.s && ld -macosx_version_min 11.0.0 -o hello_world_1mpossiblecode hello_world_1mpossiblecode.o -lSystem -syslibroot `xcrun -sdk macosx --show-sdk-path` -e _start -arch arm64 && ./hello_world_1mpossiblecode
.global _start
.align 2

_start: mov X0, #1
        adr X1, helloworld
        mov X2, #13
        mov X16, #4
        svc 0

        mov X0, #0
        mov X16, #1
        svc 0

helloworld:
        .ascii "Hello World!\n"
