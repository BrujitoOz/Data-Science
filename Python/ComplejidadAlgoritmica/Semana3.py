#Semana 3: divide y venceras
#%%
# Ejercicio 1: hallar maximo valor
def HallaMaxValorWdivYvenceras(arr, inicio, final):
  if inicio == final:
    return arr[inicio]
  med = (inicio + final) // 2
  izq = HallaMaxValorWdivYvenceras(arr, inicio, med)
  der = HallaMaxValorWdivYvenceras(arr, med+1, final)
  if izq > der:
    return izq
  else:
    return der
arr = [5,13,100,1,88]
print(HallaMaxValorWdivYvenceras(arr, 0, 5-1))
#%%
# Ejercicio 2: contador palabras
def contar_palabras(a):
    if len(a) == 1: 
        return len(a[0].split(" "))
    else:
        m = len(a)//2
        i = contar_palabras(a[:m])
        d = contar_palabras(a[m:])
        return i+d
texto = ["hola quiero comer mi comidita"]
print("El numero de palabras en el texto es:",contar_palabras(texto))
#%%
# Ejercicio 3: quicksort
def Pivot(arr, i, f):
  p = arr[i]
  left = i + 1
  right = f
  while left <= right:
    if arr[left] <= p:
      left+=1
    elif p <= arr[right]:
      right-=1
    else:
      arr[right], arr[left] = arr[left], arr[right]
  if i != right:
    arr[right], arr[i] = arr[i], arr[right]
  return right
def Quick(arr, i, f):
  if i < f:
    p = Pivot(arr, i, f)
    Quick(arr, i, p -1)
    Quick(arr, p + 1, f)
def QuickSort(arr, n):
  Quick(arr, 0, n-1)
arr = [7,3,9,6,2,4,8,1,5]
n = len(arr)
QuickSort(arr, n)
print(arr)
#%%
# Ejercicio propuesto: encontrar la suma subsecuencia mas grande
def FB(arr):
  smax = 0
  for i in range (len(arr)):
      sumaact = 0
      for j in range(i, len(arr)):
        sumaact += arr[j]
        if sumaact > smax:
          smax = sumaact
  print(smax)
arr = [-2, 11, -4, 13, -5, -2]
FB(arr) 
#%%
# Ejercicio propuesto: multiplicar
def MultiplicarWdivYvenc(n1,n2,d):
  if d==1:
    return n1*n2
  med = d // 2
  p = 10 ** d
  n1izq = n1 // p
  n1der = n1 % p
  n2izq = n2 // p
  n2der = n2 % p
  z1 = MultiplicarWdivYvenc(n1izq, n2izq, med) * p
  z2 = (MultiplicarWdivYvenc(n1izq,n2der, med)+MultiplicarWdivYvenc(n1der,n2izq,med)) * p
  z3 = MultiplicarWdivYvenc(n1der,n2der,med)
  return z1+z2+z3
print(MultiplicarWdivYvenc(60, 30, 2))

#%%
# Ejercicio propuesto: multiplicar matrices con recursividad TODO
