JMP start
start:
; A prev1, B prev2, C act

MOV D, 232

MOV [D], 1
INC D
MOV [D], 1
INC D
MOV [D], 1
INC D

MOV A, 1
MOV B, 1
MOV C, 1

loop:
ADD A, B
PUSH A
MOV A, B
MOV B, C
POP C

MOV [D], C
INC D
CMP D, 244
JBE loop