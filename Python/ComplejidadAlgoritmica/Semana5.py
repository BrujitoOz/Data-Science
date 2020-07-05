# Semana 5: ucs, dls, ids
#%%
s, a, b, c, g = 0, 1, 2, 3, 4 
G1 = [
  [(a, 1), (b, 5), (c, 15)],
  [(s, 1), (4, 10)],
  [(s, 5), (g, 5)],
  [(s, 15), (g, 5)],
  [(a, 10), (b, 5), (c, 5)]
]
G2 = [
  [(1, 387), (21, 602)], #A
  [(0, 387), (5, 634), (6, 447), (15, 456)],#B
  [(3, 409)],#C
  [(2, 409), (8, 659), (12, 458)],#D
  [(19, 698), (13, 745)],#E
  [(1, 634), (9, 474), (14, 757)],#G
  [(1, 447), (14, 702), (18, 587), (8, 251)],#H
  [(13, 382), (12, 445)],#I
  [(6, 251), (3, 659)],#J
  [(16,611), (5, 474)],#L
  [(11, 910), (16, 498), (20, 1296), (19, 1062)],#M
  [(10, 910)],#N
  [(3, 458), (15, 292), (7, 445)],#O
  [(4, 745), (21, 745), (7, 382)],#P
  [(17, 521), (6, 702), (5, 757)],#R
  [(1, 456), (12, 292)],#S
  [(10, 498), (9, 611)],#T
  [(14, 521)],#U
  [(6, 587)],#V
  [(4, 698), (10, 1062), (20, 866)],#X
  [(10, 1296), (19, 866)],#Y
  [(0, 602), (13, 745)]#Z
]
from random import randint
def generarGrafoConPesosL(n,m):
    mat = [[] for i in range(n)]
    for j in range(m):
        v1 = randint(0, n - 1)
        v2 = randint(0, n - 1)
        w = randint(1, 10)
        adyacentes = [x[0] for x in mat[v1]]
        while(v2 in adyacentes or v2 == v1):
            v1 = randint(0, n - 1)
            v2 = randint(0, n - 1)
        mat[v1] += [(v2,w)]
    return mat
names1 = ['S', 'A', 'B', 'C', 'G']
names2 = ['A','B','C','D','E','G','H','I','J','L','M', 'N', 'O','P', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']

# uniform cost search
from heapq import heappush, heappop
from math import inf
def ucs(G, start, end):
  n = len(G)
  visited = [False] * n
  weight  = [inf] * n
  path    = [None] * n
  queue   = []
  heappush(queue, (0, start))
  weight[start] = 0
  while len(queue) > 0:
    PesoPadre, NodoPadre = heappop(queue)
    if NodoPadre == end:
      break
    if visited[NodoPadre]:
      continue
    visited[NodoPadre] = True
    for NodoHijo, PesoHijo in G[NodoPadre]:
      if not visited[NodoHijo]:
        NuevoPeso = PesoPadre + PesoHijo
        if NuevoPeso < weight[NodoHijo]:
          weight[NodoHijo] = NuevoPeso
          path[NodoHijo]   = NodoPadre
          heappush(queue, (NuevoPeso, NodoHijo))
  return path, weight

path, weights = ucs(G1, s, g)
last = g

while last != None:
    print(names1[last], last, weights[last])
    last = path[last] 

print(" ")
# deep limit search
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
path, x = dls(G2, 1, 13, 14)
last = 13
while last != None:
  print(names2[last], last)
  last = path[last] 

print(" ")
# iterative deepsearch
def ids(G, s, t):
    for i in range(len(G)):
        path, found = dls(G, s, t, i)
        if found:
            return path, i
path, limit = ids(G2, 1, 13) 
print("couta",limit)
last = 13
while last != None:
    print(names2[last], last)
    last = path[last] 
