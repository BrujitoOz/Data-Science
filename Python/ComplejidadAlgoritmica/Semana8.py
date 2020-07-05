#%%
Graph = [
  [(1, 10), (4, 10)],#A 0
  [(0, 10), (2, 10), (3, 10), (5, 10)],#B 1
  [(0, 10), (1, 10), (3, 10), (4, 10)],#C 2
  [(1, 10), (2, 10), (4,  10), (5, 10)],#D 3
  [(0, 10), (2, 10), (3, 10)],#E 4
  [(1, 10), (3, 10)] #F 5
]
names = ['A', 'B', 'C', 'D', 'E', 'F']
from heapq import heappush, heappop
from math import inf
def ucs(G, start, end):
  n = len(G)  # 1
  visited = [False] * n #2 
  weight  = [inf] * n # 2
  path    = [None] * n # 2
  queue   = [] # 1
  heappush(queue, (0, start)) # 2
  weight[start] = 0 # 2
  while len(queue) > 0: # 1
    print("queue",queue) # 1
    PesoPadre, NodoPadre = heappop(queue) # 1
    if NodoPadre == end: # 1
      break  # 1
    if visited[NodoPadre]: # 1
      continue # 1
    visited[NodoPadre] = True # 2
    for NodoHijo, PesoHijo in G[NodoPadre]: # b^k
      if not visited[NodoHijo]: # 2  +    10
        NuevoPeso = PesoPadre + PesoHijo # 2 +    8
        if NuevoPeso < weight[NodoHijo]: # 2 +    6
          weight[NodoHijo] = NuevoPeso # 2
          path[NodoHijo]   = NodoPadre # 2
          heappush(queue, (NuevoPeso, NodoHijo)) # 2
  return path, weight

path, weights = ucs(Graph, 0, 5)
last = 5
while last != None:
    print(names[last], last, weights[last])
    last = path[last]

#%%
GrafoCamino = [
    [(1, 5)], # 1
    [(0, 5), (2, 20)], # 2
    [(1, 20)] # 3
]
GrafoTren = [
    [(2, 30, 5)], # 1
    [(2, 3, 6), (2, 6, 7)], # 2
    [(0, 0, 5)] # 3
]
GrafoTren = [
    [(2, 35)], # 1
    [(2, 9), (2, 13)], # 2
    [(0, 5)] # 3
]
Grafo1 = [
    [(1, 3)], # 1
    [(0, 3), (2, 2)], # 2
    [(1, 2), (3, 4)], # 3
    [(2, 4), (4, 5)], # 4
    [(3, 5)] # 5 
]

Grafo2Camino = [
    [(1, 3)], # 1
    [(0, 3), (2, 5)], # 2
    [(1, 5), (3, 6)], # 3
    [(2, 6), (4, 4)], # 4
    [(3, 4)] # 5
]
Grafo2Tren = [
    [], # 1
    [], # 2
    [(1, 1, 1), (3, 0, 1)], # 3, suma tiempo espera + tiempo que tarda en llegar al otro nodo
    [], # 4
    [] # 5
]
Grafo2Tren = [
    [], # 1
    [], # 2
    [(1, 2), (3, 1)], # 3
    [], # 4
    [] # 5
]
Grafo3 = [
    [(1, 20), (4, 3)], # 1
    [(0, 20), (2, 5), (3, 2), (4, 1)], # 2
    [(1, 5)], # 3
    [(1, 2)], # 4
    [(0, 3), (1, 1)] # 5
]
names = ['1', '2', '3', '4', '5']
from heapq import heappush, heappop
from math import inf
def ucs(G, start, end):
  n = len(G)  # 1
  visited = [False] * n #2 
  weight  = [inf] * n # 2
  path    = [None] * n # 2
  queue   = [] # 1
  heappush(queue, (0, start)) # 2
  weight[start] = 0 # 2
  while len(queue) > 0: # 1
    PesoPadre, NodoPadre = heappop(queue) # 1
    if NodoPadre == end: # 1
      break  # 1
    if visited[NodoPadre]: # 1
      continue # 1
    visited[NodoPadre] = True # 2
    for NodoHijo, PesoHijo in G[NodoPadre]: # b^k
      if not visited[NodoHijo]: # 2  +    10
        NuevoPeso = PesoPadre + PesoHijo # 2 +    8
        if NuevoPeso < weight[NodoHijo]: # 2 +    6
          weight[NodoHijo] = NuevoPeso # 2
          path[NodoHijo]   = NodoPadre # 2
          heappush(queue, (NuevoPeso, NodoHijo)) # 2
  return path, weight
"""
path, weights = ucs(Grafo1, 0, 4)
print("Grafo Opcion 1 de lucas, tiempo de ir caminando de 1 a 5: ", weights[4])
print("  ")

path, weights = ucs(Grafo2Camino, 0, 4)
print("Grafo Opcion 2 de lucas, tiempo de ir caminando de 1 a 5: ", weights[4])
print("  ")

path, weights = ucs(Grafo2Tren, 2, 3)
print("Grafo Opcion 2 de lucas, tiempo de ir en tren de 2 a 3: ", weights[3])
print("  ")

path, weights = ucs(Grafo3, 0, 4)
print("Grafo Opcion 2 de lucas, tiempo de ir caminando de 1 a 5: ", weights[4])
"""

def dls(G, s, t, limit):
  n = len(G)
  path = [None]*n
  visited = [False]*n
  def dfs(G, u, limit):
    if limit == 0 or u == t and not visited[u]:
      visited[u] = True
      return
    if not visited[u]:
      visited[u] = True
      for v,w in G[u]:
        if not visited[v]:
          path[v] = u
          dfs(G, v, limit - 1)
  dfs(G, s, limit)
  return path, visited[t]
path, x = dls(Grafo1, 1, 3, 5)
last = 3
while last != None:
  print(names[last], last)
  last = path[last]