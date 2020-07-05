JMP start:
num1: DB 120
num2: DB 80

comp1: DB 20
comp2: DB 20

pot: DB 5
ini: DB 1
n1: DB 2

ascii: DB 48

start:

;CALL suma
;CALL print3cifras
;CALL Comparacion
;CALL funcionpotencia

JMP end
end:
HLT

condicion:
MOV C, 1
JMP end

Comparacion:
MOV A, [comp1]
MOV B, [comp2]
CMP A, B
JE condicion
JMP end
RET


suma:
MOV A, [num1]
ADD A, [num2]
RET


funcionpotencia:
MOV A, [n1]
MOV D, [ini]
loop:
INC D
MUL [n1]
CMP D, [pot]
JB loop
JMP end
RET



print2cifras:
MOV B, A
DIV 10
MUL 10
SUB B, A
ADD B, [ascii]
PUSH B
DIV 10
ADD A, [ascii]
PUSH A
POP B
MOV D, 232
MOV [D], B
INC D
POP A
MOV [D], A
INC D
MOV [D], 32
INC D
RET

print3cifras:
MOV B, A
MOV C, B
DIV 100
MUL 100
SUB B, A
MOV A, B
DIV 10
MUL 10
SUB B, A
ADD B, [ascii]
PUSH B
DIV 10
ADD A, [ascii]
PUSH A
MOV A, C
DIV 100
ADD A, [ascii]
PUSH A
MOV D, 232
POP A
MOV [D], A
INC D
POP A
MOV [D], A
INC D
POP A
MOV [D], A
INC D
RET