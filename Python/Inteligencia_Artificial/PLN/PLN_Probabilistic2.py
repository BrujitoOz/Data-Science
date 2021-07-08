import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.text import Text
import os
# recuperando 
ruta = "C:/Users/Hernan/OneDrive - Universidad Peruana de Ciencias/Documents/Programacion/Python/Inteligencia_Artificial/PLN/Corpus2.txt"
archivo = "Corpus2.txt"
# leyendo
lectordetexto = PlaintextCorpusReader(os.getcwd(), archivo,encoding='utf8')
temp = lectordetexto.words()
texto = Text(temp)
print(Text(texto))

print(texto.count('inteligencia'))

print(texto.index('inteligencia'))

print(texto.concordance('inteligencia'))

#texto.dispersion_plot(['inteligencia', 'maquina'])

# frecuencia de las palabras
frecuencia = {'inteligencia':texto.count('inteligencia'),
'maquinas': texto.count('maquina'),
'ciencias': texto.count('ciencias')}
print(frecuencia)
print(len(frecuencia))
print(frecuencia.keys())
print(frecuencia.values())
print(frecuencia.items())

texto2 = ['inteligencia', 'maquinas', 'ciencias', 'inteligencia', 'maquinas']
fdist = nltk.FreqDist(texto2)
print(fdist)

print(list(nltk.FreqDist.keys(fdist)))

print(list(nltk.FreqDist.values(fdist)))
