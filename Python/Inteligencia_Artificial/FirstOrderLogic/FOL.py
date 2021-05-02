# Base de conocimiento
from kanren import *
hijo = Relation()
esposo = Relation()
facts(hijo,
("David", "Sabino"),
("Rene", "Sabino"),
("Hernan", "Sabino"),
("Angie", "David"),
("Marcelo", "Rene")
)

facts(esposo,
("Sabino", "Rosalia"),
("David", "Flore"),
("Rene", "Nelith")
)
# Motor de inferencia
# Para todo hijo existe al menos un hermano
# Vx, Vy, Ey hijo(x,y) y hijo(y,z) --> hermano(x,z)
H1 = var()
H2 = var()
def hermano(x,z):
    y = var()
    return conde(  ( hijo(x,y), hijo(z,y)   ))

l = run(0, (H1, H2), hermano(H1,H2) )
#print(l)
print( [(x,y) for x,y in run(0,(H1,H2), hermano(H1,H2)) if x!=y] )