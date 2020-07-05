# Semana 11: Programacion Dinamica
# Se puede aplicar en problemas que se sobreponen o con subestructuras optimas
#%%
def fibonacci(n):
    global contador1
    contador1 += 1
    if n == 1 or n == 0:
        return n
    return fibonacci(n-2) + fibonacci(n-1)
def fibonacciDP(n):
    cache = [-1 for _ in range(n+1)]
    def f(n):
        global contador2
        contador2 += 1
        if n == 0 or n == 1:
            cache[0] = 0
            cache[1] = 1
        else:
            f(n-1)
            cache[n] = cache[n-1] + cache[n-2]
    f(n)
    return cache[n]

contador1 = 0
print("Fibonacci recursivo(20):", fibonacci(20))
print("Numero de iteraciones:" ,contador1)
print()
contador2 = 0
print("Fibonacci programacion dinamica:", fibonacciDP(20))
print("Nuevo numero de iteraciones:", contador2)
#%%
from math import inf
def change(M, n):
    k = len(M)
    cache = [inf for _ in range(n+1)]
    s = [0 for _ in range(n+1)]
    cache[0] = 0
    for valor in range(1, n+1):
        minimo = inf
        for i in range(k):
            if M[i] <= valor:
                if 1 + cache[valor - M[i]] < minimo:
                    minimo = 1 + cache[valor - M[i]]
                    moneda = i
        cache[valor] = minimo
        s[valor] = M[moneda]
    return cache, s

def monedas(d, n):
    cache = [-1 for _ in range(n+1)]
    k = len(d)
    s = [0 for _ in range(n+1)]
    def cambio(valor):
        if valor < 0:
            return inf
        if valor == 0:
            return 0
        if cache[valor] != -1:
            return cache[valor]
        minimo = inf
        for i in range(k):
            if 1 + cambio(valor - d[i]) < minimo:
                minimo = 1 + cambio(valor- d[i])
                moneda = i
        cache[valor] = minimo
        s[valor] = d[moneda]
        return cache[valor], s[valor]
    print(cambio(35))
n = 35
M = [1, 5, 10, 20, 25, 50]

c, s = change(M, n)
print("Se necesitan %d en total"%(c[n]))
while n > 0:
    print("1 monedas en %d centimos"%(s[n]))
    n -= s[n]

#%%
valor = [3, 4, 5, 6]
pesos = [2, 3, 4, 5]
w= 5
n = len(valor)
def mochila2(pesos, valor, cap, n):
    cache = [[0 for _ in range(cap+1)] for _ in range(n+1)]
    for i in range(n+1):
        for j in range(cap+1):
            if i == 0 or j == 0:
                cache[i][j] = 0
            elif pesos[i - 1] <= j:
                cache[i][j] = max(valor[i-1] + cache[i-1][j-pesos[i-1]], cache[i-1][j])
            else:
                cache[i][j] = cache[i-1][j]
    return cache[i][j]
print(mochila2(pesos, valor, w, n))
# %%
valor = [3, 4, 5, 6]
pesos = [2, 3, 4, 5]
w= 5
n = len(valor)
tabla = [[-1 for _ in range(w+1)] for j in range(n+1)]
def mochila1(pesos, valor, cap, n):
    if n == 0 or cap == 0:
        return 0
    if tabla[n][cap] != -1:
        return tabla[n][cap]
    if pesos[n-1] <= cap:
        tabla[n][cap] = max(valor[n-1] + mochila1(pesos, valor, cap-pesos[n-1], n-1)
        , mochila1(pesos, valor, cap, n-1))
        return tabla[n][cap]
    elif pesos[n-1] > cap:
        tabla[n][cap] = mochila1(pesos, valor, cap, n-1)
        return tabla[n][cap]
#print(mochila1(pesos, valor, w, n))


def mochila3(pesos, valor, cap, n):
    if n == 0 or cap == 0:
        return 0
    if pesos[n-1] > cap:
        return mochila3(pesos, valor, cap, n-1)
    else:
        return max(valor[n-1] + mochila1(pesos, valor, cap - pesos[n-1], n-1), mochila1(pesos, valor, cap, n-1))
print(mochila3(pesos, valor, w, n))

#%%
def ackerman(m,n):
    if m == 0:
        return n+1
    if m > 0 and n == 0:
        return ackerman(m-1, 1)
    return ackerman(m-1, ackerman(m,n-1))

print(ackerman(5,7))


#conprogramacion dinamic
#https://www.geeksforgeeks.org/ackermanns-function-using-dynamic-programming/

def Ackermann(m, n): 
    # creating 2D LIST 
    cache = [[0 for i in range(n + 1)] for j in range(m + 1)] 
    for rows in range(m + 1): 
        for cols in range(n + 1): 
            # base case A ( 0, n ) = n + 1 
            if rows == 0:        
                cache[rows][cols] = cols + 1
            # base case  A ( m, 0 ) =  
            # A ( m-1, 1) [Computed already] 
            elif cols == 0: 
                cache[rows][cols] = cache[rows-1][1] 
            else: 
                # if rows and cols > 0 
                # then applying A ( m, n ) =  
                # A ( m-1, A ( m, n-1 ) )  
                r = rows - 1
                c = cache[rows][cols-1] 
                # applying equation (2)  
                # here A ( 0, n ) = n + 1 
                if r == 0:     
                    ans = c + 1
                elif c <= n: 
                    # using stored value in cache 
                    ans = cache[rows-1][cache[rows][cols-1]] 
                else: 
                    # Using the Derived Formula  
                    # to compute mystery values in O(1) time 
                    ans = (c-n)*(r) + cache[r][n] 
                cache[rows][cols] = ans 
    return cache[m][n] 
print(Ackermann(5,7))          
