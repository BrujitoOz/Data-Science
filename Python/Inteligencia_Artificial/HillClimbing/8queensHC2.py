import copy
import random
import numpy as np

def Inicializacion(N):
  Individuos = {}
  Individuos = np.random.choice(range(1,N+1),N,replace=True)
  return Individuos

def CalcHeuristica(tablero):
  heuristica = 0
  for i in range(len(tablero)):
    unitario = 0
    for j in range(len(tablero)):
      unitario += 1
      #Horizontal                     #Diagonal
      if tablero[i] == tablero[j] or abs(tablero[i]-tablero[j]) == abs(i - j):
        unitario -= 1
      
    #print(unitario)
    heuristica += unitario
  
  return heuristica/2

def CreaPosibilidades(indi, N, i):
  ind1 = []
  probH=[]
  ind1 = copy.copy(indi)
  for j in range(1,N+1):
    ind1[i] = j
    probH.append(CalcHeuristica(ind1))
    #print(probH)
  return probH

def HillClimbing(indi,N,probH):
    vez = 0
    hOriginal=0
    
    while hOriginal != 28:
      if vez > 7:
        vez = 0
        continue
      print("VEZ", vez)
      probH=[]
      max=0
      pos=0
      print("Lista: ",indi)
      hOriginal = CalcHeuristica(indi)
      print("Heuristica original: ", hOriginal)
      
      probH = CreaPosibilidades(indi, N, vez)
      print("Probabilidad")
      print(probH)
      
      for i in range(N):
        if probH[i] > max:
          max = probH[i]
          pos = i
          
      print("MAX: ",max)
      print("MIN: ",min)
      if hOriginal<max:
        print("entre h<max")
        indi[vez] = pos+1

      if hOriginal >= max:
        indi[vez] = random.randint(1,N)
      #else:
       # print("entre h>max")
        #vez += 1
        #continue      
      vez += 1
      probH=[]
      hOriginal = CalcHeuristica(indi)
      print("lista: ")
      print(indi)
    print("REPUESTA!", indi)


N = 8
#indi = [2,4,7,4,8,5,5,2]
indi = Inicializacion(N)
print(indi)
probH = []
Sol = HillClimbing(indi, N, probH)
print(Sol)