# Semana 13: Programacion Dinamica en Grafos 2
#%%
# Camino minimo Johnson: 1 invocacion de la iteracion Bellman Ford y N de dijkstra
# Encuentra el camino mas corto entre todos los pares de vertices de un grafo dirigido disperso
# Acepta aristas negativas, no ciclos de peso negativo
from math import inf
import heapq as hq
def BellmanFord(G, s):
  n = len(G)
  d = [inf for _ in range(n)]
  d[s] = s
  for _ in range(n-1):
    for u in range(n):
      for v, w in G[u]:
        dist = d[u] + w 
        if dist < d[v]:
          d[v] = dist
  return d
def Dijkstra(G, s): 
  n = len(G)
  visited = [False for _ in range(n)]
  weights = [inf for _ in range(n)]
  path = [None for _ in range(n)]
  queue = []
  weights[s] = 0
  hq.heappush(queue, (0, s))
  while len(queue) > 0:
    g, u = hq.heappop(queue)
    visited[u] = True
    for v, w in G[u]:
      if not visited[v]:
        f = g + w 
        if f < weights[v]: 
          weights[v] = f
          path[v] = u
          hq.heappush(queue, (f, v)) 
  return weights, path

def Jhonson(G):
  n = len(G) 
  G.append([(n-1,0)])
  pb = BellmanFord(G,n)
  Gp = [[] for _ in range(n)]
  for u in range(n):
    for v,Ce in G[u]:
      print(pb[u],pb[v])
      Gp[u].append((v, Ce + pb[u] - pb[v]))
  
  paths =[[] for _ in range(n)]
  weights = [[] for _ in range(n)]
  for u in range(n):
    weights[u], paths[u] = Dijkstra(Gp, u)
  return paths, weights
  
def printPath(path, weights, f, F):
    if f != -1:
        printPath(path, weights, path[f], F)
        print(f, end=' ')
    else:
        print('W=%2.0f:'%(weights[F]), end=' ')

# Grafo 2
a, b, c, d, e, f = 0, 1, 2, 3, 4, 5
G = [
  [(b, -2)],
	[(c, -1)],
	[(a, 4), (d, 2), (e, -3)],
	[],
	[],
	[(d, 1),(e, -4)]
]
# Grafo 1
a, b, c, d = 0, 1, 2, 3
G = [
  [(b, -3), (d, 2)],
  [(a, 5), (c, 3)],
  [(a, 1)],
  [(a, -1), (c, 4)]
]
# Grafo clase pasada con peso negativo
G = [
  [(1, 6), (3, 7)],
  [(2, 5), (3, 8), (4, -4)],
  [(1, -2), (4, 7)],
  [(2, -3), (4, 9)],
  [(0, 2)]
]
p, w = Jhonson(G)
print(p)
print(w)

#%%
from math import inf
def bfs(graph, start, end, path):
  size = len(graph)
  visited = [False for _ in range(size)]
  queue = []
  queue.append(start)
  visited[start] = True
  while len(queue) > 0:
    idx = queue.pop(0)
    for jdx, val in enumerate(graph[idx]):
      if not visited[jdx] and val > 0:
        visited[jdx] = True
        queue.append(jdx)
        path[jdx] = idx
  return visited[end]

def FordFulkerson(G,start, end):
  n = len(G)
  max_flow = 0
  path = [None for i in range(n)]
  dgraph = [[0 for x in range(n)] for x in range(n)]
  rgraph = [[0 for x in range(n)] for x in range(n)]
  for u, node in enumerate(G):
    for v,w in node:
      dgraph[u][v] = w

  while bfs(dgraph, start, end, path):
    min_flow = inf
    temp = end 
    while temp!=start: 
      min_flow= min(min_flow,dgraph[path[temp]][temp])      
      temp = path[temp]
    print("min_flow ",min_flow)
    max_flow += min_flow
    temp = end
    while temp != start:
      dgraph[path[temp]][temp] -= min_flow
      rgraph[path[temp]][temp] += min_flow
      temp = path[temp]
  return max_flow, rgraph

# Grafo 2
G = [
  [(1, 9), (2, 12)],
  [(2, 6),(3,9),(4,4),(5,3)], 
  [(3, 2), (4, 6),(5,3)],
  [(4, 2),(6,7)],
  [(5, 2),(6,8)],
  [(6, 5)],
  []
]
# Grafo 3 Ejercicio
i, a, b, c, d, e, f = 0, 1, 2, 3, 4, 5, 6
G = [
  [(a, 6), (b, 4), (c, 1)],
  [(d, 4)],
  [(c, 3), (d, 1), (e, 3)],
  [(e, 4)],
  [(f, 4)],
  [(f, 9)],
  []
]
# Grafo 1
s, a, b, c, d, t = 0, 1, 2, 3, 4, 5
G = [
  [(a, 16), (c, 13)],
  [(b, 12), (c, 10)],
  [(c, 9), (t, 20)],
  [(a, 4), (d,14)],
  [(b, 7), (t, 4)],
  []
]
m, f = FordFulkerson(G,s,t) 
for x in range(len(f)):
  print(f[x])
print(m) 
print(f)


# %%
