# Semana 1: analisis de algoritmos
#%%
#Ejercicio 1: uso de arreglos 1
from random import randint
def GenerateArr1(n):
  arr = []
  for i in range(n):
    arr.append(randint(1,100))
  return arr
def GenerateArr2(n):
  arr = [0] * n
  for i in range(n):
    arr[i] = randint(1, 100)
  return arr
def GenerateArr3(n):
  return [randint(1, 100) for _ in range(n)]
def ShowArray(arr):
  print(arr)
def MinValueArray(arr):
  return min(arr)
def MediaValueArray(arr):
  m = 0
  for i in arr:
    m+= i
  return m / len(arr) 
def Ocurrencias(arr):
  repeti = [0] * 100
  for i in arr:
    repeti[i] += 1
  return repeti
arr = GenerateArr3(5)
ShowArray(arr)
#%%
#Ejercicio 2: uso de arreglos 2
arr = [0] * 100
arr = [i for i in range(0, 100)]
print(arr)
#%%
#Ejercicio 3: sudoku, pedir al usuario ingresar una grilla de sudoku y devolver verdadero si es correcto, falso en caso contrario
def Sudoku(s):
  for i in range(len(s)):
    Colums = [False] * len(s)
    for j in range(len(s)):
      if Colums[s[i][j]-1] == False:
        Colums[s[i][j]-1] = True
      else:
        return False
  for i in range(len(s)):
    Rows = [False] * len(s)
    for j in range(len(s)):
      if Rows[s[j][i]-1] == False:
        Rows[s[j][i]-1] = True
      else:
        return False
  return True
s = [[1, 2, 3, 4],
     [3, 4, 1, 2],
     [2, 3, 4, 1],
     [4, 1, 2, 3]]
print(Sudoku(s))
s = [[1, 2, 3, 4],
     [3, 4, 4, 2],
     [2, 3, 1, 1],
     [4, 1, 2, 3]]
print(Sudoku(s))
s = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
     [4, 5, 6, 7, 8, 9, 1, 2, 3],
     [7, 8, 9, 1, 2, 3, 4, 5, 6],
     [2, 3, 4, 5, 6, 7, 8, 9, 1],
     [5, 6, 7, 8, 9, 1, 2, 3, 4],
     [8, 9, 1, 2, 3, 4, 5, 6, 7],
     [3, 4, 5, 6, 7, 8, 9, 1, 2],
     [6, 7, 8, 9, 1, 2, 3, 4, 5],
     [9, 1, 2, 3, 4, 5, 6, 7, 8]]
print(Sudoku(s))
#%%
#Ejercicio 4: criba erastotenes
from math import sqrt
n = 100
Primos = [True] * n
Primos[0] = False
Primos[1] = False
for i in range(2, int(sqrt(n))):
  for j in range(i, int(n/i)):
    if Primos[i]:
      Primos[i*j] = False
for i in range(100):
  if Primos[i]:
    print(i)