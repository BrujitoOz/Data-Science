# Semana 10: Arbol de expansion minima (MST)
# Un arbol de expansion es un grafo no dirigido, conexo, sin ciclos
#%%
# Kruskal: elige la arista menos pesada
# si la arista forma un ciclo en el grafo eliminarla, si no añadirla
from graphviz import Graph
import heapq as hq
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


# Grafo 1 diapositiva
s, a, b, c, d, e, t = 0, 1, 2, 3, 4, 5, 6
G = [
	[(a, 2), (b, 5), (c, 4)],
	[(s ,2), (b, 2), (d, 7)],
	[(s, 5), (a, 2), (c, 1), (d, 4), (e, 3)],
	[(s, 4), (b, 1), (e, 4)],
	[(a, 7), (b, 4), (e, 1), (t, 5)],
	[(b, 3), (c, 4), (d, 1), (t, 7)],
	[(d, 5), (e, 7)]
]
# Grafo 2 diapositiva
s, a, b, c, d, e, f, g, t = 0, 1, 2, 3, 4, 5, 6, 7, 8
G = [
	[(a, 4), (b, 9)], # s
	[(s, 4), (b, 11), (d, 9)], # a
	[(s, 9), (a ,11), (c, 7), (e, 7)], # b
	[(b, 7), (d, 2), (e, 6)], # c
	[(a, 9), (c, 2), (f, 4), (g, 7)], # d
	[(b, 1), (c, 6), (f, 2)], # e
	[(d, 4), (e, 2), (g, 15), (t, 11)], # f
	[(d, 7), (f, 15), (t, 10)], # g
	[(f, 11), (g, 10)] # t
]
# Grafo 3 conexiones computadoras
a, b, c, d, e, f = 0, 1, 2, 3, 4, 5
G = [
	[(b, 2), (c, 3), (e, 6)],
	[(a, 2), (e, 2), (f, 3)],
	[(a, 3), (d, 5), (e, 1)],
	[(c, 5), (e, 5), (f, 6)],
	[(a, 6), (b, 2), (c, 1), (d, 5), (f, 4)],
	[(b, 3), (e, 4), (d, 6)]	
]
# Grafo 4 letras
a, b, c, d, e, f = 0, 1, 2, 3, 4, 5
G = [
    [(b, 1), (c, 5)],
    [(a, 1), (e, 6), (f, 7)],
    [(a, 5), (d, 3), (e, 2)],
    [(c, 3), (e, 4), (f, 1)],
    [(b, 6), (c, 2), (d, 4), (f, 3)],
    [(b, 7), (d, 1), (e, 3)]
]


T, c = Kruskal(G)
print(T)
print(c)
#%%
# Prim: comienza vacio
# empieza con un vertice v cualquiera
# despues vas al vertice con menor coste
# luego al otro vertice más cerca de estos dos, y asi hasta tener los n vertices
from graphviz import Graph
import heapq as hq
from math import inf
def Prim(G):
	n = len(G)
	visited = [False for _ in range(n)] 
	dist = [inf for _ in range(n)]
	Tree = [-1 for _ in range(n)]
	dist[0] = 0
	queue = []
	hq.heappush(queue, (0, 0))
	while len(queue) > 0:
		_,u = hq.heappop(queue)
		if visited[u]:
			continue
		visited[u] = True
		for v, w in G[u]:
			if not visited[v] and w < dist[v]:
				Tree[v] = u
				dist[v] = w
				hq.heappush(queue, (w, v))
	return Tree
def Dot(T):
	n = len(T)
	dot = Graph()
	for i in range(n):
		dot.node(str(i))
	for i in range(n):
		if T[i] >= 0:
			dot.edge(str(i), str(T[i]))
	dot.graph_attr['rankdir'] = 'BT'
	return dot

# Grafo 1 diapositiva
s, a, b, c, d, e, t = 0, 1, 2, 3, 4, 5, 6
G = [
	[(a, 2), (b, 5), (c, 4)],
	[(s ,2), (b, 2), (d, 7)],
	[(s, 5), (a, 2), (c, 1), (d, 4), (e, 3)],
	[(s, 4), (b, 1), (e, 4)],
	[(a, 7), (b, 4), (e, 1), (t, 5)],
	[(b, 3), (c, 4), (d, 1), (t, 7)],
	[(d, 5), (e, 7)]
]
# Grafo 2 diapositiva
s, a, b, c, d, e, f, g, t = 0, 1, 2, 3, 4, 5, 6, 7, 8
G = [
	[(a, 4), (b, 9)], # s
	[(s, 4), (b, 11), (d, 9)], # a
	[(s, 9), (a ,11), (c, 7), (e, 7)], # b
	[(b, 7), (d, 2), (e, 6)], # c
	[(a, 9), (c, 2), (f, 4), (g, 7)], # d
	[(b, 1), (c, 6), (f, 2)], # e
	[(d, 4), (e, 2), (g, 15), (t, 11)], # f
	[(d, 7), (f, 15), (t, 10)], # g
	[(f, 11), (g, 10)] # t
]
# Grafo 3 conexiones computadoras
a, b, c, d, e, f = 0, 1, 2, 3, 4, 5
G = [
	[(b, 2), (c, 3), (e, 6)],
	[(a, 2), (e, 2), (f, 3)],
	[(a, 3), (d, 5), (e, 1)],
	[(c, 5), (e, 5), (f, 6)],
	[(a, 6), (b, 2), (c, 1), (d, 5), (f, 4)],
	[(b, 3), (e, 4), (d, 6)]	
]

G = [
    [(1, 1), (2, 5)],
    [(0, 1), (4, 6), (5, 7)],
    [(0, 5), (3, 3), (4, 2)],
    [(2, 3), (4, 4), (5, 1)],
    [(1, 6), (2, 2), (3, 4), (5, 3)],
    [(1, 7), (3, 1), (4, 3)]
]
T = Prim(G)
print(T)
Dot(T)


# %%
