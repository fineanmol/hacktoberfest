// Reference: https://www.youtube.com/watch?v=gfmRrPjnEw4&t=7672s&ab_channel=freeCodeCamp.org
// Online simulator: https://cpulator.01xz.net/?sys=arm-de1soc
// LANGUAGE: Assembly ARMv7
// AUTHOR: Mastermind-sap
// GITHUB: https://github.com/Mastermind-sap

.global _start
_start:
	MOV R0,#1 //output in standard output of computer #0->standard input #2->standard error
	LDR R1,=message
	LDR R2,=len
	MOV R7,#4 // on interrupt the os looks to r7 finds 4 which is for printing checks r0,r1,r2 and does the operation
	SWI 0 //software interrupt
	
	MOV R7,#1 //exit program
	SWI 0
	
.data
message:
		//.ascii ->not null terminated
		//.asciz or .string ->null terminated
		.asciz "hello world \n"
len=.-message //stores length of message in variable len