# Semana 12: Programacion dinamica en grafos 1
#%%
# Bellman Ford: Para grafos dirigidos ciclicos con aristas con peso negativo
from math import inf
import heapq
def BellmanFord(G, s):
  n = len(G)
  d = [inf for _ in range(n)]
  p = [None for _ in range(n)]
  d[s] = 0
  for _ in range(n-1):
    for u in range(n):
      for v, w in G[u]:
        if d[v] > d[u] + w:
          d[v] = d[u] + w
          p[v] = u
  for u in range(n):
    for v, w in G[u]:
      if d[v] > d[u] + w:
        print("ohhh nooo, ciclo negativo")
        return
  return p, d

def Dijkstra(G, s):
  n = len(G)
  visited = [False for _ in range(n)]
  weights = [inf for _ in range(n)]
  path = [None for _ in range(n)]
  queue = []
  weights[s] = 0
  heapq.heappush(queue, (0, s))
  while len(queue) > 0:
    g, u = heapq.heappop(queue)
    visited[u] = True
    for v, w in G[u]:
      if not visited[v]:
        f = g + w
        if f < weights[v]:
          #print(f,weights[v])
          weights[v] = f
          path[v] = u
          heapq.heappush(queue, (f, v))
  return path, weights

L =['A','B','C','D','E','F']
def printpath(path,dist, f, F):
  if f!=None:
    printpath(path,dist, path[f],F)
    print(L[f], end =' ')
  else:
    print('W=%2.0f:' %(dist[F]), end =' ')

# Grafo 1 negativo diapositiva
G = [
  [(1, 6), (3, 7)],
  [(2, 5), (3, 8), (4, -4)],
  [(1, -2), (4, 7)],
  [(2, -3), (4, 9)],
  [(0, 2)]
]
# Grafo 1 Diapositiva 2
a, b, c, d, e, f = 0, 1, 2, 3, 4, 5
G = [
  [(b, 1), (c, 2), (d, 8)],
  [(e, 3)],
  [(d, 5), (e, 3), (f, 8)],
  [(f, 12)],
  [(f,4)],
  []
]
# Grafo 2 Diapositiva 2
G = [
  [(2, -2)],
  [(0, 4), (2, 3)],
  [(3, 2)],
  [(1, -1)]
]
print("Resultado con BellmanFord")
p, d = BellmanFord(G, 0)
print(p)
print(d)
for n in range(len(G)):
  printpath(p,d,n,n)
  print()
print("Resultado con dijkstra")
p, w = Dijkstra(G, 0)
print(p)
print(w)
for n in range(len(G)):
    printpath(p, w, n, n)
    print()

#%%
# Floyd Warshall: camino minimo a todos los destinos desde todos los nodos, grafo no dirigido
from math import inf
def Floydwarshall(G):
  n = len(G)
  d = [[inf for _ in range(n)] for _ in range(n)]
  p = [[-1 for _ in range(n)] for _ in range(n)]
  for u in range(n):
    d[u][u] =0
    for v, w in G[u]:
      d[u][v]=w
      p[u][v]=u
  for k in range(n):
    for i in range(n):
      for j in range(n):
        f = d[i][k] + d[k][j]
        if d[i][j] > f:
          d[i][j] = f
          p[i][j] = k
  return p, d

# Grafo 1 Diapositiva 2
a, b, c, d, e, f = 0, 1, 2, 3, 4, 5
G = [
  [(b, 1), (c, 2), (d, 8)],
  [(e, 3)],
  [(d, 5), (e, 3), (f, 8)],
  [(f, 12)],
  [(f,4)],
  []
]
# Grafo 2 Diapositiva 2
G =[
  [(2, -2)],
  [(0, 4),(2, 3)],
  [(3, 2)],
  [(1, -1)]
]
L =['A','B','C','D','E','F']
def printPath(path, weights, f, F):
    if f != -1:
        printPath(path, weights, path[f], F)
        print(L[f], end=' ')
    else:
        print('W=%2.0f:'%(weights[F]), end=' ')

p, d = Floydwarshall(G) 
print(p)
print(d)
for n in range(len(G)):
  printPath(p[0], d[0], n, n)
  print()


# %%
