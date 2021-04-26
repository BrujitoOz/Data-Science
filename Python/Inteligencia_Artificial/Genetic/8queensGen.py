import numpy as np
import random

class Genetic8Queens:
  def __init__(self, N, numPoblacion, generacion):
    self.N = N
    self.numPoblacion = numPoblacion
    self.generacion = generacion

  def Inicializacion(self, pob, N):
    Individuos = {}
    for i in range(pob):
      Individuos[i] = np.random.choice(range(1,N+1),N,replace=True)
    return Individuos

  def CalcHeuristica(self, tablero):
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

  def Idoneidad(self, ProbSeleccion, arrH):
    for i in range(self.numPoblacion):
      ProbSeleccion.append((arrH[i]/sum(arrH))*100)
    return ProbSeleccion

  def Pesos(self, newPop, indi, ProbSeleccion):
    for i in range(self.numPoblacion):
      newPop[i] = (random.choices(indi, ProbSeleccion)[0]) #Agregado [0] porque choices devuelve un grupo de resultados
    return newPop

  def Cruce(self, sons, newPop, info):
    for cruz in range(0, self.numPoblacion, 2):
      pivot = random.randint(0,N-1)
      if info: print(pivot)
      son1 = []
      son2 = []
      for i in range(N):
        if i < pivot:
          son1.append(newPop[cruz][i])
          son2.append(newPop[cruz+1][i])
        else:
          son1.append(newPop[cruz+1][i])
          son2.append(newPop[cruz][i])
      sons[cruz] = son1
      sons[cruz+1] = son2
    if info: print(newPop)
    return sons

  def Mutacion(self, newPop, info):
    nMutaciones = 5
    chance = 0.5
    for i in range(len(newPop)):
      mutar =random.random()
      if mutar < chance:
        for m in range(nMutaciones):
          pivot = random.randint(0,N-1)
          mutacion = random.randint(1,N)
          if info: print("son:",i," mutacion(pos:",pivot," -> " ,mutacion,")")
          newPop[i][pivot] = mutacion
    if info: print(newPop)
    self.generacion += 1
    return newPop

  def Sol(self):
    indi = self.Inicializacion(self.numPoblacion, self.N)
    info = False
    end = False
    while True:
      print("Generacion: ", self.generacion)
      arrH = []
      for i in range(self.numPoblacion):
        arrH.append(self.CalcHeuristica(indi[i]))
      print(arrH)
      #Check for End
      for i in range(self.numPoblacion):
        if arrH[i] >= 28:
          end = True
      if end: break

      #Calculo de %
      ProbSeleccion = []
      ProbSeleccion = self.Idoneidad(ProbSeleccion, arrH)
      if info: print(ProbSeleccion)

      #Pesos
      newPop = {}
      newPop = self.Pesos(newPop, indi, ProbSeleccion)
      if info: print(indi)
      if info: print(newPop)

      #Cruce
      sons = {}
      newPop = self.Cruce(sons, newPop, info)
      
      #Mutacion
      indi = self.Mutacion(newPop, info)

    print(indi)
    resultado = 0
    for i in range(len(arrH)):
      if arrH[i] == 28:
        resultado = indi[i]
    print("Respuesta Final: ",resultado)

N = 8 # 8 reinas
numPoblacion = 800
generacion = 1

ia = Genetic8Queens(N, numPoblacion, generacion)
ia.Sol()