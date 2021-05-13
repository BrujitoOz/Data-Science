import pandas as pd
from kanren import *
# Preprocesamiento
archBueno = pd.read_excel("Bueno.xlsx")
archIngrediente = pd.read_excel("Ingredientes.xlsx")
archTipo = pd.read_excel("Tipo.xlsx")
# capturamos las columnas
P3 = archBueno['Producto_B'].values
E3 = archBueno['Enfermedad_E'].values

P1 = archIngrediente['Producto_I'].values
M1 = archIngrediente['Menu_I'].values

M2 = archTipo['Menu_T'].values
T2 = archTipo['Tipo_T'].values

# Base de conocimiento
# Matematica representado base de conocimiento: bueno(P,E)  ingrediente(P,Plato) estipo(Plato,Tipo)

ingrediente = Relation()
estipo = Relation()
bueno = Relation()

P = var()
E = var()

for i in range(len(P3)):
    fact(bueno, P3[i], E3[i])

#print(run(0,(P,E),bueno(P,E)  ))

for i in range(len(P1)):
    fact(ingrediente, P1[i], M1[i])
#print(run(0,(P,E),ingrediente(P,E)  ))

for i in range(len(M2)):
    fact(estipo, M2[i], T2[i])
#print(run(0,(P,E),estipo(P,E)  ))

# Modelo matematico para el motor de inferencia
# Todo alimento es bueno para alguna enfermedad y este alimento es ingrediente de algun menu
# y el menú es un tipo de plato que se puede servir
# modelo matematico
# para todo Alimento, existe Enfermedad, existe Menú, Exist Tipo
# regla: bueno(Alimento, enfermendad) e ingrediente(Alimento, Menu)
# y estipo(Menu, Tipo) => recomienda(Menu,Tipo)

# Motor de inferencia implementada
Alimento = var()
Menu = var()
Tipo = var()
Enfermedad = "stress"
print(run(0, (Menu, Tipo),  bueno(Alimento, Enfermedad), ingrediente(Alimento,Menu), estipo(Menu, Tipo)  ))