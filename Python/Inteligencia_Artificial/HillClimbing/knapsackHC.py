import copy
import random

class Item:
    def __init__ (self, id=0, v=0, w=0):
        self.id = id
        self.v = v
        self.w = w

class Solution:
    def __init__ (self, cap):
        self.cap = cap
        self.maxv = 0
        self.best = []
    
    def __addItems(self):
        self.items = [
            Item(1, 8, 5), 
            Item(2, 7, 6), 
            Item(3, 12, 10), 
            Item(4, 6, 4), 
            Item(5, 2, 1), 
            Item(6, 3, 1)
        ]
    
    def __hillClimbing(self):
        for i, _ in enumerate(self.items):
            w = 0
            v = 0
            end = False
            init = copy.deepcopy(self.items)
            
            random.shuffle(init)
            
            start = max(init, key=lambda x: x.v)
            init.remove(start)

            sol = []
            sol.append(start)
            w += start.w
            v += start.v
            #print("Inicio: %i %i"%(start.v, start.w))
            while not end:
                bestIt = sol[-1] #Ultimo valor de la solucion
                auxW = 9999
                auxV = 0
                for item in init:
                    # evlua que no pase capacidad, 
                    if(item.w + w) <= self.cap and (item.v + v) > auxV and (item.w + w) < auxW:
                        auxV = item.v
                        auxW = item.w
                        bestIt = item
                    # si no se pudo agregar un nuevo bestIt 
                    if bestIt != sol[-1]:
                        w += bestIt.w
                        v += bestIt.v
                        init.remove(bestIt)
                        sol.append(bestIt)
                    else:
                        if v > self.maxv:
                            self.best = copy.deepcopy(sol)
                            self.maxv = v
                        print("Maximo hasta ahora %i"%(self.maxv))
                        print("Valor: {}, Peso: {}".format(v, w, self.cap))
                        end = True
        print("\nMejor solucion:")
        print("Valor: {}, Peso: {} de {}".format(sum([x.v for x in self.best]), sum([x.w for x in self.best]), self.cap))
        for item in self.best:
            print('\t', item.id, item.v, item.w)

    def Load(self):
        self.__addItems()

    def Solve(self):
        self.__hillClimbing()


sol = Solution(16)
sol.Load()
sol.Solve()