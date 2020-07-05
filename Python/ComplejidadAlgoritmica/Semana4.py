# Semana 4: grafos, busqueda dfs y bfs
#%%
# BFS y DFS
from queue import Queue
class GraphAdyacentList:
  def __init__(self, V):
    self.V = V
    self.Graph = [[] for i in range(V)]
  def AddEdge(self, u, v):
    self.Graph[u].append(v)
  def PrintGraph(self):
    for i in range(self.V):
      print("head: ", i, end="")
      for j in self.Graph[i]:
        print(" -> ", j, end="")
      print()
  def BFS(self, Vindex):
    visited = [False for _ in range(self.V)]
    #visited = [False] * self.V
    path = [None for _ in range(self.V)]
    queue = Queue()
    visited[Vindex] = True
    queue.put(Vindex)
    while not queue.empty():
      Vindex = queue.get()
      print(Vindex, " ")
      for i in self.Graph[Vindex]:
        if not visited[i]:
          path[i] = Vindex
          visited[i] = True
          queue.put(i)
    print()
    print(path)
  def _DFS(self, Vindex, visited, path):
    visited[Vindex] = True
    print(Vindex, " ")
    for i in self.Graph[Vindex]:
      if not visited[i]:
        path[i] = Vindex
        self._DFS(i, visited, path)
  def DFS(self, Vindex):
    path = [None for _ in range(self.V)]
    visited = [False for _ in range(self.V)]
    #visited = [False] * self.V
    self._DFS(Vindex, visited, path)
    print(path)
    print()
#%%
# Tarea: Implemente un algoritmo de fuerza bruta que encuentre un camino para salir del laberinto
def imprimir(lab):
  for i in lab:
    for j in i:
      print(j, end="")
    print()
lab = [
  [1,1,1,1],
  [1,0,1,1],
  [1,1,1,1],
  [1,1,2,1]
]
imprimir(lab)
def submat(lab, i, j):
  nor, sur, est, oes = -1, -1, -1, -1
  n = len(lab)
  if i != 0:
    nor = lab[i-1][j]
  if i < n-1:
    sur = lab[i+1][j]
  if j != 0:
    oes = lab[i][j-1]
  if j < n-1:
    est = lab[i][j+1]
  sm = [nor, sur, oes, est]
  return sm
def solve(lab, i, j):
  sm = submat(lab, i, j)
  lab[i][j] = -1
  for k in range(len(sm)):
    if sm[k] == 2:
      if k == 0:
        print("norte")
      if k == 1:
        print("sur")
      if k == 2:
        print("oeste")
      if k == 3:
        print("este")
      quit()
  for k in range(len(sm)):
    if sm[k] == 1:
      if k == 0:
        print("norte")
        solve(lab, i-1,j)
      elif k == 1:
        print("sur")
        solve(lab, i+1,j)
      elif k == 2:
        print("oeste")
        solve(lab, i,j-1)
      elif k == 3:
        print("este")
        solve(lab, i, j+1)

i , j = 0, 0
solve(lab, i, j)
#%%
# Tarea: Implemente un algoritmo de recorrido en amplitud (BFS) que encuentre un camino para salir dellaberinto 
from queue import Queue
def MazeBFS():
  global found
  rq.put(sr)
  cq.put(sc)
  visited[sr][sc] = True
  vacio = rq.empty()
  while not vacio:
    r = rq.get()
    c = cq.get()
    if matrix[r][c] == 2:
      found = True
      break
    for i in range(4):
      rr = r + dr[i]
      cc = c + dc[i]
      if rr < 0 or cc < 0:
        continue
      if rr >= R or cc >= C:
        continue
      if visited[rr][cc]:
        continue
      if matrix[rr][cc] == 0:
        continue
      rq.put(rr)
      cq.put(cc)
      visited[rr][cc] = True
      previ[rr][cc] = [r,c]
  if found:
    return previ
  return []

matrix = [
  [1, 1, 1, 0, 1, 1, 1],
  [1, 0, 1, 1, 1, 0, 1],
  [1, 0, 1, 1, 1, 1, 1],
  [1, 1, 0, 0, 1, 1, 1],
  [0, 1, 0, 1, 1, 0, 1]
]
R, C = len(matrix), len(matrix[0])
sr, sc = 0, 0
er, ec = 0, 6
matrix[er][ec] = 2
rq, cq = Queue(), Queue()
found = False
visited = [[False for _ in range(C)] for _ in range(R)]
previ = [[None for _ in range(C)] for _ in range(R)]
dr = [-1,1,0,0]
dc = [0,0,1,-1]

paths = MazeBFS()
def GetPath(er, ec):
  path = []
  path.append([er,ec])
  while paths[er][ec] != None:
    aux = paths[er][ec]
    path.append(aux)
    er = aux[0]
    ec = aux[1]
  path.reverse()
  return path
print(GetPath(er,ec))
#%%
# Tarea: Implemente un algoritmo de recorrido en profundidad (DFS) que encuentre un camino para salir del laberinto
def MazeDFS(matrix, r, c, er, ec, visited, path):
  global R, C
  if matrix[r][c] == 0:
    return
  if visited[r][c]:
    return
  else:
    visited[r][c] = True
    path[r][c] = 2
    if r + 1 < R and matrix[r+1][c] == 1:
      MazeDFS(matrix, r+1, c, er, ec, visited, path)
    if c + 1 < C and matrix[r][c+1] == 1:
      MazeDFS(matrix, r, c + 1, er, ec, visited, path)
    if r - 1 >= 0 and matrix[r-1][c] == 1:
      MazeDFS(matrix, r - 1, c, er, ec, visited, path)
    if c - 1 >= 0 and matrix[r][c-1] == 1:
      MazeDFS(matrix, r, c-1, er, ec, visited, path)
    if r  == er and c  == ec:
      print(path)
      return
    path[r][c] = 0

matrix = [
  [1, 1, 1, 0, 1, 1, 1],
  [1, 0, 1, 1, 1, 0, 1],
  [1, 0, 1, 1, 1, 1, 1],
  [1, 1, 0, 0, 1, 1, 1],
  [0, 1, 0, 1, 1, 0, 1]
]
R, C = len(matrix), len(matrix[0])
sr, sc = 0, 0
er, ec = 0, 6
visited = [[False for _ in range(C)]for _ in range(R)]
path = [[0 for _ in range(C)]for _ in range(R)]
MazeDFS(matrix, sr, sc, er, ec, visited, path)

#%%
from random import randint
def generarGrafos(n,m):
    mat =[[]for i in range(n)]
    for j in range(m):
        v1 = randint(0, n-1)
        v2 = randint(0, n-1)
        while(v2 in mat[v1] or v2 == v1):
            v1 = randint(0, n-1)
            v2 = randint(0, n-1)
        mat[v1] += [v2]
    return mat 

g = generarGrafos(5,8)
print(g)

def listAristas(t):
    t1 = []
    for i in range(len(t)):
        for j in t[i]:  
            t1 += [(i,j)]
    return t1
la = listAristas(g)
print(la)

def BFS(g,s):
    visitado = [False]*len(g)
    cola = []
    cola += [s]
    aux = []
    visitado[s]=True
    while cola:
        s = cola.pop(0)
        aux+=[s]
        for i in g[s]:
            if not visitado[i]:
                cola += [i]
                visitado[i] = True
    return aux

def DFS(g,s):
    visitado = [False]*len(g)
    pila = []
    pila += [s]
    aux = []
    visitado[s]=True
    while pila:
        s = pila.pop()
        aux+=[s]
        for i in g[s]:
            if not visitado[i]:
                pila += [i]
                visitado[i] = True
    return aux

BFS(g,0)
print('hola')
DFS(g,0)

def listBFS(g):
    t1 = []
    for i in range(len(g)-1):
        t1 += [(g[i],g[i+1])]
    return t1

ltBFS = listBFS(BFS(g,0))
print(ltBFS)

litDFS = listBFS(DFS(g,0))
print(litDFS)
