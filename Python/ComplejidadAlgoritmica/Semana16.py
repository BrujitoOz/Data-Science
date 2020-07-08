utilidad = [3,4,5,6]
pesos = [2,3,4,5]
W = 15
n = len(utilidad)
# implementacion en python
def papanoel(pesos, valor, c, n):
    cache =[[0 for j in range(c+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(c+1):
            if i == 0 or j == 0:
                cache[i][j] = 1
            elif pesos[i-1] <= j:
                cache[i][j] = max(valor[i-1] * cache[i-1][j-pesos[i-1]], cache[i-1][j])
            else:
                cache[i][j]=cache[i-1][j]
    return cache[i][j], cache

rpta, m = papanoel(pesos, utilidad, W, n)
print("La utilidad maxima es:", rpta)
print("Tiempo de ejecucion:", len(m) * len(m[0]))



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
    max_flow += min_flow
    temp = end
    while temp != start:
      dgraph[path[temp]][temp] -= min_flow
      rgraph[path[temp]][temp] += min_flow
      temp = path[temp]
  return max_flow, rgraph

s,sa,sb,s0,sab,da,db,d0,dab,t=0,1,2,3,4,5,6,7,8,9
G = [
    [(sa,44),(sb,31),(s0,42),(sab,38)],
    [(da,inf),(dab,inf)],
    [(db,inf),(dab,inf)],
    [(da,inf),(db,inf),(d0,inf),(dab,inf)],
    [(dab,inf)],
    [(t,37)],
    [(t,33)],
    [(t,40)],
    [(t,40)],
    []
]


max_flow, g_flujo = FordFulkerson(G, s,t)
print("El grafo flujo es:")
for x in range(len(g_flujo)):
  print(g_flujo[x])
print("El flujo maximo es:",max_flow)


from math import sqrt, floor, inf
import heapq as hq
# Primero el algoritmo Kruskal
def find(s, a):
	if s[a] < 0:
		return a
	else:
		granpa = find(s, s[a])
		s[a] = granpa
		return granpa
def union(s, a, b):
	pa = find(s, a)
	pb = find(s, b)
	if pa == pb: 
		return
	if s[pa] <= s[pb]:
		s[pa] += s[pb]
		s[pb] = pa
	elif s[pb] < s[pa]:
		s[pb] += s[pa]
		s[pa] = pb
def ordenarAristas(G):
	cola = []
	for u in range(len(G)):
		for v, w in G[u]:
			hq.heappush(cola, (w, u, v))
	return cola
def Kruskal(G):
	cola = ordenarAristas(G)
	n = len(G)
	raices = [-1] * n
	T = [-1 for _ in range(n)]
	c = 0
	while len(cola) > 0:
		w, u, v = hq.heappop(cola)
		if find(raices, u) != find(raices, v):
			union(raices, u, v)
			T.append((u, v, w))
			c += w
	return T,c


class Faro:
	def __init__(self, n, x, y):
		self.n = n
		self.x = x
		self.y = y
# input
def CoordenadasFaroles():
	Tablero = Faro(0, 0, 0)
	Faro1 = Faro(1, 1, 3)
	Faro2 = Faro(2, 3, 1)
	Faro3 = Faro(3, 2, 2)
	Faro4 = Faro(4, 3, 5)
	Faro5 = Faro(5, 1, 7)
	Faro6 = Faro(6, 8, 6)
	Faro7 = Faro(7, 5, 7)
	Faro8 = Faro(8, 5, 3)
	Faro9 = Faro(9, 8, 1)
	Faro10 = Faro(10, 8, 4)
	Faro11 = Faro(11, 10, 3)
	Faro12 = Faro(12, 12, 1)
	Faro13 = Faro(13, 13, 3)
	Faro14 = Faro(14, 12, 5)
	Faro15 = Faro(15, 12, 7)
	# lista
	ArrFaros = [Tablero, Faro1, Faro2, Faro3, Faro4, Faro5, Faro6, Faro7, Faro8, Faro9, Faro10, Faro11, Faro12, Faro13, Faro14, Faro15]
	return ArrFaros

Faros = CoordenadasFaroles()

# generar el grafo usando la formula de la distancia
def BuildGraph(N):
	G = [[] for _ in range(N + 1)] 
	for i in range(N + 1):
		for j in range(i + 1, N + 1):
			W = floor( sqrt( pow(Faros[j].x - Faros[i].x, 2) + pow(Faros[j].y - Faros[i].y, 2) )  ) + 2 # ojo
			#print(Faros[i].n, Faros[j].n, W)
			G[i].append( (j, W)  )
	return G

# Obtenemos el grafo
N = 15
G = BuildGraph(N)

# imprimen (x, y, w)
# T desde T[0] a T[15] son igual -1 porque el Tablero no tiene padres
def ImprimirSinTuplas(T):
	for i in range(16, 31):
		for j in range(len(T[i])):
			print(T[i][j], end=" ")
		print()

# Este seria el grafo exacto
G = [
	[(1, 5), (2, 5), (3, 4), (4, 7), (5, 9), (6, 12), (7, 10), (8, 7), (9, 10), (10, 10), (11, 12), (12, 14), (13, 15), (14, 15), (15, 14)], 
	[(2, 4), (3, 3), (4, 4), (5, 6), (6, 9), (7, 7), (8, 6), (9, 9), (10, 9), (11, 11), (12, 13), (13, 14), (14, 13), (15, 13)], 
	[(3, 3), (4, 6), (5, 8), (6, 9), (7, 8), (8, 4), (9, 7), (10, 7), (11, 9), (12, 11), (13, 12), (14, 11), (15, 11)], 
	[(4, 5), (5, 7), (6, 9), (7, 7), (8, 5), (9, 8), (10, 8), (11, 10), (12, 12), (13, 13), (14, 12), (15, 12)], 
	[(5, 4), (6, 7), (7, 4), (8, 4), (9, 8), (10, 7), (11, 9), (12, 11), (13, 12), (14, 11), (15, 12)], 
	[(6, 9), (7, 6), (8, 7), (9, 11), (10, 9), (11, 11), (12, 14), (13, 14), (14, 13), (15, 15)], 
	[(7, 5), (8, 6), (9, 7), (10, 4), (11, 5), (12, 8), (13, 7), (14, 6), (15, 6)], 
	[(8, 6), (9, 8), (10, 6), (11, 8), (12, 11), (13, 10), (14, 9), (15, 11)], 
	[(9, 5), (10, 5), (11, 7), (12, 9), (13, 10), (14, 9), (15, 9)], 
	[(10, 5), (11, 4), (12, 6), (13, 7), (14, 7), (15, 6)], 
	[(11, 4), (12, 7), (13, 7), (14, 6), (15, 7)], 
	[(12, 4), (13, 5), (14, 4), (15, 5)],
	[(13, 4), (14, 6), (15, 3)],
	[(14, 4), (15, 5)], 
	[(15, 7)],
	[]
]
# Se llama a Kruskal
T, c = Kruskal(G)
print("conexiones:")
print("x-y-costo")
ImprimirSinTuplas(T)
print("Costo(cable necesario economicamente):", c)

