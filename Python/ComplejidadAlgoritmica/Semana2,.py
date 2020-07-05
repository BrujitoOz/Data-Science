# Semana 2: espacio de busqueda, fuerza bruta y backtracking
#%%
#Ejercicio 1: implementar bubble sort
arr = [7,3,9,6,2,4,8,1,5]
for i in range(0, len(arr)-1):
  for j in range(i+1, len(arr)):
    if arr[i] > arr[j]:
      arr[i], arr[j] = arr[j], arr[i]
print(arr)
#%%
#Ejercicio 2: funcion polinomica
from random import randint
def generar(n):
    c = []
    for i in range(n):
        c.append(randint(1,101))
    return c
print("--------------- generar")
a = generar(10)
print(a)
def polinomio(a,x0):
    n = len(a)
    s = 0
    print("para x=" + str(x0))
    for i in range(n):
        indice = n - i - 1
        s += a[i] * (x0 ** indice)
        print(str(a[i])+"*x"+str(indice),end="+")
    print("=",end="")
    return s
print("--------------- polinomio")
print(polinomio([5,3,1],3))
#%%
#Ejercicio 3: criptoaritmetica fuerza bruta
# SEND + MORE = MONEY
import time
u = 1
d = 10
c = 100
m = 1000
mm = 10000
def distinct(*args):
    return len(set(args)) == len(args)
start = time.time()
for S in range(1,10):
  for E in range(0,10):
    for N in range(0,10):
      for D in range(0,10):
        for M in range(1,10):
          for O in range(0,10):
            for R in range(0,10):
              for Y in range(0,10):
                if distinct(S, E, N, D, M, O, R, Y):
                  send = m*S + c*E + d*N + u*D
                  more = m*M + c*O + d*R + u*E
                  money = mm*M + m*O + c*N + d*E + u*Y
                  if (send + more == money):
                    end = time.time()
                    print(send, more, money, " tiempo: ", end-start)
                    
#%%
#Ejercicio 3: criptoaritmetica backtracking
import time
def ArmaNumeros(word, nch):
  l = len(word)
  nums = 0
  for ch in word:
    l-=1
    nums += nch[ch]*10**l
  return nums
def CA(a, b, c, chars, digs, nch):
  # Cuando n sea 0 significa que cada letra ya tiene asignado una valor aunque no cumplan la suma
  n = len(chars) 
  if n == 0:
    # segun los numeros que se asignaron a cada letra 
    na = ArmaNumeros(a, nch)
    nb = ArmaNumeros(b, nch)
    nc = ArmaNumeros(c, nch)
    return na + nb == nc
  else:
    ch = chars[-1]
    for i in range(len(digs)):
      nch[ch] = digs[i]
      if CA(a, b, c, chars[:n-1],digs[:i]+digs[i+1:], nch):
        na = ArmaNumeros(a, nch)
        nb = ArmaNumeros(b, nch)
        nc = ArmaNumeros(c, nch)
        print (na, nb, nc)
a = 'SEND'
b = 'MORE'
c = 'MONEY'
# crea una lista de todas las letras sin repetirse
chars = list(set(a+b+c))
# chars = [S, E, N, D, M, O, R, Y] no necesariamente en orden
# envia las 3 palabras, lista de letras, lista de 0-9, el {} es un diccionario que se usara para asignar numeros a las letras tipo {N : 3, M : 2} 
start = time.time()
CA(a, b, c, chars, [n for n in range(10)], {})
end = time.time()
print("Tiempo: ", end - start)
#%%
# Ejercicio 4: Problema del pastor
def Mueve(p, r, a):
  r.remove(p)
  a.append(p)
def Evalua(a, b):
  if sum(a) == 1 and sum(b) == 5:
    aux = max(b)
    Mueve(aux, b, a)
  elif sum(a) == 4 and sum(b) == 2:
    aux = min(a)
    Mueve(aux, a, b)
  else:
    aux = max(a)
    Mueve(aux, a, b)
  ResolverAcertijo(a, b)
def ResolverAcertijo(a, b):
  if sum(a) == 0 and sum(b) == 6: # Termina cuando los 3 personajes llegan a la derecha
    return a, b
  else:
    Evalua(a, b)
a = [1,2,3] # Isla izquierda
b = [] # Isla derecha
print("Maggie=3, Veneno=2, Perro=1")
print(a, b)
ResolverAcertijo(a, b)
print(a, b)
#%%
#Ejercicio propuesto: encontrar coincidencias
def StringMatch(texto, busca):
  coincidencias = []
  for i in range(len(texto)):
    if texto[i] == busca[0]:
      for j in range(len(busca)):
        if busca[j] != texto[i+j]:
          break
      coincidencias.append(i)
  return coincidencias
p = StringMatch("abracadabracalamazoo", "rac")
print(p)
#%%
#Ejercicio propuesto: nqueens
def draw(board):
    n = len(board)
    print("%s+"%("+---"*n))
    for i in range(n):
        for j in range(n):
            if board[i] == j:
                print("| Q ", end="")
            else:
                print("|   ", end="")
        print("|")
        print("%s+"%("+---"*n))
draw([1, 3, 0, -1])
def check(board, row, col):
    #n = len(board)
    for i in range(row):
        if board[i] == col:
            return False
        d = row - i
        if board[i] + d == col:
            return False
        if board[i] - d == col:
            return False
    return True
def nqueens(board, row):
    n = len(board)
    if row < n:
        for col in range(n):
            if check(board, row, col):
                board[row] = col
                nqueens(board, row + 1)
    else:
        draw(board)
n = 4
board = [-1]*n
nqueens(board, 0)