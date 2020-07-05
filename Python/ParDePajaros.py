I = 13
a = [3, 3, 3, 6, 9, 12, 9, 9, 6, 3, 3, 3, 3]
a.insert(0,0)
def Pajaros(x, y):
    global contador1
    contador1+=1
    if y < 0 or y > 300:
        return inf
    if x == I:
        return abs(a[x]-y)
    return  min(Pajaros(x+1,y+1), Pajaros(x+1,y-1)) + abs(a[x]-y)
    
from math import inf
def PajarosDP(x, y):
    I = 13
    a = [3, 3, 3, 6, 9, 12, 9, 9, 6, 3, 3, 3, 3]
    a.insert(0,0)
    cache = [[-1 for _ in range(301)] for _ in range(I+1)]
    def Pajaros(x, y):
        global contador2
        contador2+=1
        if y < 0 or y > 300:
            return inf
        if x == I:
            cache[x][y] = abs(a[x]-y)
            return cache[x][y]
        if cache[x][y] != -1:
            return cache[x][y]
        cache[x][y] = min(Pajaros(x+1,y+1), Pajaros(x+1,y-1)) + abs(a[x]-y)
        return cache[x][y]
    Pajaros(x, y)
    return cache[0][0]

contador1, contador2 = 0, 0
print("Sin DP:")
print("Resultado:", Pajaros(0,0))
print("Iteraciones:", contador1)

print("Con DP:")
print("Resultado:", PajarosDP(0,0))
print("Iteraciones:", contador2)