JMP start
n: DB 10
fibo1: DB 0
fibo2: DB 0
start:
MOV D, 232
MOV [D], 0
MOV [fibo2], 0
INC D
MOV [D], 1
MOV [fibo1], 1
INC D
MOV B, 2

loop:
MOV C, 0
ADD C, [fibo2]
ADD C, [fibo1]
MOV [D], C

MOV C, [fibo1]
MOV [fibo2], C
MOV C, [D]
MOV [fibo1], C
INC D
INC B
CMP B, [n]
JB loop

HLT