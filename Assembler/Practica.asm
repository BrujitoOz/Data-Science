; Actualizar el valor de variables en memoria RAM
; Nota: Si no alcanzan los registros A,B,C,D se debe escribir
;       en variables en RAM con instrucción MOV. El resto de
;       instrucciones no puede escribir en RAM.

    JMP start    ; Salta a etiqueta start

nume1:     DB 10        ;
nume2:  DB 25        ;
suma:    DB 0        ;

start:
    ; Ejemplo 1 - Resguardo y Recuperación de valor original
    MOV A, [nume1]        ; Resguarda valor nume1 en registro A
    MOV [nume1], 28        ; Reemplaza nume1 por 28
    MOV [nume1], A        ; Recupera valor original en nume1
    MOV A, 0        ; Limpia registro A

    ; Ejemplo 2 - Intercambio de valor de 2 variables en RAM
    MOV A, [nume1]        ; Resguarda valor nume1 en registro A
    MOV B, [nume2]        ; Resguarda valor nume2 en registro B
    MOV [nume1], B        ; Reemplaza nume1 por nume2
    MOV [nume2], A        ; Reemplaza nume2 por nume1
    MOV A, 0        ; Limpia registro A
    MOV B, 0        ; Limpia registro B

    ; Ejemplo 3 - Suma nume1 y nume2 y graba en var suma en RAM
    MOV A, [nume1]        ; Copia valor nume1 en registro A
    ADD A, [nume2]        ; Suma nume2 a registro A
    MOV [suma], A        ; Copia resultado en var suma en RAM
    
    HLT