"""
#%%
dias = {"Lunes":1,
        "Martes":2,
        "Miercoles":3,
        "Jueves":4,
        "Viernes":5,
        "Sabado":6,
        "Domingo":7}
dias_mayus = {}
for clave,valor in dias.items():
    dias_mayus[clave.upper()] = valor
dias = dias_mayus
print(dias)
#%%
dias_o = []
for clave in dias:
    if "o" in clave:
        dias_o.append(clave)
print(dias_o)
#%%
def resta(a,b):
    return a-b
#%%
def minusculas(texto):
    return texto.lower()
print(minusculas("ASD"))
#%%
def suma_o_resta(a,b,modo):
    if modo == "suma":
        return a+b
    elif modo == "resta":
        return a-b
    else:
        print("no valido")
print(suma_o_resta(12,12,"suma"))
print(suma_o_resta(12,32,"resta"))
print(suma_o_resta(1,12,"m"))
#%%
def invertir_palabra(frase):
    palabras = frase.split(" ")
    return " ".join(palabras[::-1])
print(invertir_palabra("La lluvia en sevilla"))
#%%
def es_palindromo(frase):
    frase_invertida = frase[::-1]
    for i in range(len(frase_invertida)):
        if frase[i] != frase_invertida[i]:
            return False
        return True
#%%

def simplificar_lista(lista_compleja):
    lista_simple = []
    for lista_interna in lista_compleja:
        for elemento in lista_interna:
            lista_simple.append(elemento)
    return lista_simple
lista_compleja = [
        [1,2,3],
        [4,5,6,7],
        [8,9]
]
print(simplificar_lista(lista_compleja))
"""