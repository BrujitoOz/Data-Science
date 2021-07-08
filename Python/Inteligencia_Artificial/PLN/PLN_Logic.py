import nltk
from nltk import CFG
from nltk.parse.generate import generate
import webbrowser
# gramaticas
gramatica = CFG.fromstring("""
F -> SU P
SU -> 'Juan'|'Pedro'|'Maria'|'Salgado'
P -> VT OD
P -> VI
VT -> 'ama' | 'lava' | 'peina' | 'adora'
OD -> 'Paula' | 'Antonio' | 'Sultan'
VI -> 'corre' | 'salta' | 'camina'
""")
#print("La gramatica es:", gramatica)

# punto de partida o axioma
#print("El axioma es:", gramatica.start())

# producciones de las reglas
#print("Producciones:", gramatica.productions())

# verificar si la frase "Maria ama Antonio" pertenece a la gramatica
# Generacion de lenguaje
for sentence in generate(gramatica, n=50):
    frase = ' '. join(sentence)
    #print(frase)
    if frase == "Maria ama Antonio":
        print("Pertenece a la gramatica")

# arbol derivacional
parser = nltk.ChartParser(gramatica)
for arbol in parser.parse(['Maria', 'ama','Antonio']):
    print(arbol)