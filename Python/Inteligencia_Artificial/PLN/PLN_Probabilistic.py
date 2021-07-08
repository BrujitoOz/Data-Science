# metodos basado en corpus
import nltk
from nltk.probability import *
# recuperando archivo de texto y token
from nltk import word_tokenize
# habilita esto si no se ha descargado antes
#nltk.download('punkt')
with open("TextoCorpus.txt", 'r') as tempfile:
    rawText = tempfile.read()
    tokens = word_tokenize(rawText)
print(rawText)

print(tokens)
print(set(tokens))

print(len(tokens))
print(len(set(tokens)))

# contabilizar palabras
print(tokens.count('universidad'))
print(100* tokens.count('universidad')/float(len(tokens)))
