JMP start
n1: DB 8
n2: DB 4
ascii: DB 48
start:
;Suma
MOV B, [n1]
ADD B, [n2]

;Obtener digitos
MOV A, B
DIV 10
MUL 10
SUB B, A
ADD B, [ascii];convertir ascii
PUSH B ; Poner en la pila primer numero
DIV 10
MOV B, A
ADD B, [ascii]
PUSH B ; segundo numero
;Output
MOV D, 232
POP B
MOV [D], B
INC D
POP B
MOV [D], B
INC D


;Resta
MOV B, [n1]
SUB B, [n2]

;Obtener digitos
MOV A, B
DIV 10
MUL 10
SUB B, A
ADD B, [ascii] ; convertir ascii
PUSH B
DIV 10
MOV B, A
ADD B, [ascii]; convertir ascii
PUSH B

;Output
MOV [D], 32
INC D
POP B
MOV [D], B
INC D
POP B
MOV [D], B
INC D

; Multiplicacion
MOV A, [n1]
MUL [n2]

; Obtener digitos
MOV B, A
DIV 10
MUL 10
SUB B, A
ADD B, [ascii]
PUSH B
DIV 10
MOV B, A
ADD B, [ascii]
PUSH B

;output
MOV [D], 32
INC D
POP B
MOV [D], B
INC D
POP B
MOV [D], B
INC D

; division
MOV A, [n1]
DIV [n2]

; obtener digitos
ADD A, [ascii]
PUSH A

;output
MOV [D], 32
INC D
POP A
MOV [D], A
INC D