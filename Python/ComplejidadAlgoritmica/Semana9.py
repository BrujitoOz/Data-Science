# Semana 9: Estructura de datos para Conjuntos disjuntos (UFDS)
# permite identificar o rastrear elementos particionados en diferentes grupos o sets
# util para detectar ciclos dentro de un grafo no dirigido
#%%
# Quick Find: M x N pasos, M comandos de union sobre N objetos
# Con 10^10 aristas conectando 10^9 
# Union: N - Find: 1
from graphviz import Digraph, Source
class Dottable:
    def Dot(self):
        dot = Digraph()
        for i in range(self.N):
            dot.node(str(i))
        for i in range(self.N):
            if self.sets[i]!=i:
                dot.edge(str(i),str(self.sets[i]))
        dot.graph_attr['rankdir'] = 'BT'
        return dot
class DisjointSetFind(Dottable):
    def __init__(self,n):
        self.N = n
        self.sets = [i for i in range(n)]
    def Find(self,a):
        return self.sets[a]
    def Union(self,a,b):
        pa = self.Find(a)
        pb = self.Find(b)
        for i in range(self.N):
            if self.sets[i] == pa:
                self.sets[i] = pb
ds = DisjointSetFind(10)
ds.Dot()
# ds.Union(3,4)(4,9)(8,0)(2,3)(5,6)(5,9)(7,3)(4,8)(6,1)
#%%
# Quick Union: Union y Find N pasos, y los arboles pueden ser muy altos
# Union: N plus find cost - Find: N
from graphviz import Digraph, Source
class Dottable:
    def Dot(self):
        dot = Digraph()
        for i in range(self.N):
            dot.node(str(i))
        for i in range(self.N):
            if self.sets[i] != i:
                dot.edge(str(i),str(self.sets[i]))
        dot.graph_attr['rankdir'] = 'BT'
        return dot  
class DisjointSetQUnion(Dottable):
    def __init__(self,n):
        self.N = n
        self.sets = [i for i in range(n)]
    def Find(self,a):
        x = a
        while x != self.sets[x]:
            x = self.sets[x]
        return x 
    def Union(self, a ,b):
        pa = self.Find(a)
        pb = self.Find(b)
        if pa != pb:
            self.sets[pa]=pb
ds=DisjointSetQUnion(10)
ds.Dot()
#%%
# Quick Union ponderado: evita arboles altos balanceadolos
# arboles mas pequeños debajo del mas grande
# Union: lgN plus cost find - Find lgN
from graphviz import Digraph, Source
class Dottable:
    def Dot(self):
        dot = Digraph()
        for i in range(self.N):
            dot.node(str(i))
        for i in range(self.N):
            if self.sets[i] >= 0:
                dot.edge(str(i), str(self.sets[i]))
        dot.graph_attr['rankdir'] = 'BT'
        return dot
class DisjointSetPonderado(Dottable):
    def __init__(self,n):
        self.N = n
        self.sets = [-1 for _ in range(n)]
    def Find(self,a):
        x = a
        while self.sets[x] >= 0:
            x = self.sets[x]
        return x 
    def Union(self, a, b):
        pa = self.Find(a)
        pb = self.Find(b)
        if self.sets[pa] < self.sets[pb]:
            self.sets[pb]= pa
        elif self.sets[pb] < self.sets[pa]:
            self.sets[pa]= pb
        else:
            self.sets[pb] -= 1
            self.sets[pa] = pb
ds=DisjointSetPonderado(10)
ds.Dot()
#%%
# Comprension de camino
from graphviz import Digraph, Source
class Dottable:
    def Dot(self):
        dot = Digraph()
        for i in range(self.N):
            dot.node(str(i))
        for i in range(self.N):
            if self.sets[i] != i:
                dot.edge(str(i), str(self.sets[i]))
        dot.graph_attr['rankdir'] = 'BT'
        return dot
class DisjointSetPC(Dottable):
    def __init__(self,n):
        self.N = n
        self.sets = [i for i in range(n)]      
    def Find(self,x):
        if x == self.sets[x]:
            return x
        else:
            antepasado = self.Find(self.sets[x])
            self.sets[x] = antepasado
            return antepasado
    def Union(self, a,b):
        pa = self.Find(a)
        pb = self.Find(b)
        if pa != pb:
            self.sets[pb]=pa
ds = DisjointSetPC(10)
ds.Dot()

# %%
