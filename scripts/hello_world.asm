section .msg
global _start ;must be declared for using gcc
_start: ;tell linker entry point
mov edx, l ;message length
mov ecx, txt ;message to write
mov ebx, 1 ;file descriptor (stdout)
mov eax, 4 ;system call number (sys_write)
int 0x80 ;call kernel
mov eax, 1 ;system call number (sys_exit)
int 0x80 ;call kernel

section .data

txt db 'Hello, world!',0xa ; hello world
l equ $ - txt ; get length to write