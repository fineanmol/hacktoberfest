#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>

#include"linkCat.c"

#define BUFSIZE 1024

static char*
basename(const char *path){
    char fsep = 0;
    #ifdef __unix__
        fsep = '/'; 
    #elif _WIN32
        fsep = '\\'; 
    #endif

    char *s = strrchr(path, fsep);
    if(!s) 
        return strdup(path);
    else 
        return strdup(s + 1);

}


static int 
file_exists(const char * file) {

    FILE *fptr;
    if((fptr = fopen(file, "r")) != NULL) {
        fclose(fptr);
        return 1;
    }
    return 0;
}


static void 
cat(const char*file, const int lflag, const int sflag) {

    char *pline = "";
    if(lflag)
        pline = "\033[31m%*d\033[0m  ";
    
    FILE * fptr = fopen(file, "rb");
    char st;
    int i = 0, s = 0, ch, cursor = 0, lcheck;
    do { 
        Node* buffer = NULL;
        cursor = 0;
        lcheck = 0;
        do { 
            ch = fgetc(fptr); //storing char in ch
                        
            if(ch != EOF){
                if(cursor < 1)
                    st = ch;
                if(isspace(ch) && ch != '\n')
                    lcheck++;
                if(isprint(ch) || ch == '\t'){
                    append(&buffer, ch);
                    cursor++;
                }
            } 

        } while(ch != EOF && ch != '\n'); // will continue until ch is not EOF and newline character
        
        // stripping repeated new lines
        if(sflag){
            if(s >=1){ // first empty line is ignored :)
                if(st == 10|| lcheck == cursor)
                /* if it's an empty line, it will be ignored
                   just like my crush ignored me :/ */ 
                    continue;
            } s++;
        }
        fprintf(stdout, pline, 6, ++i);
        print(buffer);
        if (ch != EOF){
            printf("\n");
        }

        if(st != 10) s= 0;
        dalloc(&buffer);
        
        //if buffers' first char is newline or CR, s is set to 0;

    } while(ch != EOF); // while ch is not end of the file
    printf("\n");
    fclose(fptr); //always close the file pointer BAKA ^_^         
}
    

static int 
arg_validate(const char* arg){
    if(!strcmp(arg, "-n")||
       !strcmp(arg, "-s")||
       !strcmp(arg, "-sn")||
       !strcmp(arg, "-ns")){
            return 1;
        }
    return 0;
}

static void 
help(){
    puts("Usage: nekomata [OPTION]... [FILE]...\
        \nConcatenate FILE to standard output.\
        \n\nOptions:\
        \n    -n   number all output lines\
        \n    -s   strip repeated empty output lines\
        \n\nExamples:\
        \n    nekomata -n file   Output file contents with line numbers\
        \n    nekomata > file    takes input from STDIN and redirects it to file\
        \n    nekomata >> file   takes input from STDIN and appends it to file\
        \n    nekomata -s file   Output file contents after stripping repeated empty lines\
        \n    nekomata -sn file  Output file contents with line numbers after stripping repeated empty lines");
}

int 
main(int argc, char**argv) {

    char *file = NULL, buffer[BUFSIZE];
    int lflag = 0, sflag = 0;

    if(argc == 1){
        while(fgets(buffer, BUFSIZE, stdin)){
            fputs(buffer, stdout);
        }

        return 0;

    } else if (argc == 2){
        if(!strcmp(argv[1], "-h")){
            help();
            return 0;
        }
        else if(!arg_validate(argv[1]))
            file = argv[1];
    } else if (argc > 2 && argc <= 4){
        for(int i = 1; i < argc; i++){
            if(!strcmp(argv[i], "-n"))
                lflag = 1;
            if(!strcmp(argv[i], "-s"))
                sflag = 1;
            if(!strcmp(argv[i], "-sn") || !strcmp(argv[i], "-ns")){
                sflag = 1;
                lflag = 1;
            }
            if(!arg_validate(argv[i]))
                file = argv[i];
        }
        
    } else{
        help();
        return 1;
    }

    if(!file_exists(file)) {
        char *exe = basename(argv[0]);
        fprintf(stderr, "%s: %s: No such file or directory", exe, file);
        free(exe);
        return 1;
    }
    cat(file, lflag, sflag);
    return 0;

}
