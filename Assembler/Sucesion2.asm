; 2, 1, 3, 1, 6, 2, 11, 6, x, y
; son dos sucesiones compuestas, se pueden separar segun si su
; posicion es par e impar
; pares 1, 1, 2, 6, y = 24
;        x1 x2 x3 x4
;          +1 +1 +1
; impares 2, 3, 6, 11, x = 18
;          +1 +3 +5 +7
;            +2 +2 +2
JMP start
start:
; Calculamos X
MOV B, 2 ; Iniciamos sucesion
MOV C, 1 ; incremento

MOV D, 0 ; bucle
.loop:
INC D
ADD B, C
ADD C, 2
CMP D, 4
JB .loop
; Se calcula que x = 18

; Imprime X
MOV A, B
DIV 10
MOV C, A
MUL 10
SUB B, A
ADD B, 48
PUSH B
MOV B, C
ADD B, 48
PUSH B

MOV D, 232
POP B
MOV [D], B
INC D
POP B
MOV [D], B
INC D
MOV [D], 32
INC D


; Calcular Y
MOV A, 1
MOV D, 1
.loop2:
MUL [D]
INC D
CMP D, 5
JB .loop2
; Y = 24

; Imprime Y
MOV B, A
DIV 10
MOV C, A
MUL 10
SUB B, A
ADD B, 48
PUSH B
MOV B, C
ADD B, 48
PUSH B

; output
MOV D, 234
MOV [D], 32
INC D
POP B
MOV [D], B
INC D
POP B
MOV [D], B
INC D

HLT