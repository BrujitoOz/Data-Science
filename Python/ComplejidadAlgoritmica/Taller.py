# Taller 1:
from itertools import product
from time import time
import matplotlib.pyplot as plt
import random
# Descifrar contraseña
# la contraseña es de tamaño 3
# Esta formadado por los numeros 3 y 7
# 1.- Indique el tamanio de busqueda
# candidatos -> n = 2 en m = 3
# tamanio de busqueda 8  O(2³)
# 2.- Implemente un programa de FB que encuentre la contrasenia, muestre la iteracion donde se encontro
A = ['5', '7'] # n = 2
m = 3 # tamanio 3
def TodosLosResultados():
  start = time()
  for i, intento in enumerate(product(A, repeat=m)):
    intento = ''.join(intento)
    print("la contraseña es: ", intento)
    print("i: ", i)
    print()
  end = time()
  t = end - start
  print("Tiempo: ", t*1000)
def DescifrarContrasenia(A, m):
  contraseña = ''.join(random.choice(A) for i in range(m))
  start = time()
  for i, intento in enumerate(product(A, repeat=m)):
    intento = ''.join(intento)
    if intento == contraseña:
      #print("encontre: ", intento)
      #print("i: ", i)
      break
  end = time()
  t = end - start
  #print("Tiempo: ", t * 1000)
  return t*1000

# 3.- Calcule el tiempo en encontrar la contrasenia en n = 5 m = 3, n = 10 m = 6, n = 15, m = 9 y dibujar la grafica
# pow(5,3) pow(10,6) pow (15,9)
def XComplejidadYTiempo():
  s = [str(i) for i in range(20)]
  complejidades, tiempos = [], []
  for n in [5, 10, 15]:
    if n == 5:
      NA = random.sample(s, 3)
      print(NA)
      comple = str(n) + '^' + '3'
      tiem = DescifrarContrasenia(NA, 3)
      complejidades.append(comple)
      tiempos.append(tiem)
    if n == 10:
      NA = random.sample(s, 6)
      print(NA)
      comple = str(n) + '^' + '6'
      tiem = DescifrarContrasenia(NA, 6)
      complejidades.append(comple)
      tiempos.append(tiem)
    if n == 15:
      NA = random.sample(s, 9)
      print(NA)
      comple = str(n) + '^' + '9'
      tiem = DescifrarContrasenia(NA, 9)
      complejidades.append(comple)
      tiempos.append(tiem)
  return complejidades, tiempos

x, y = XComplejidadYTiempo()
print(x)
print(y)
plt.title("Tiempo en funcion de la complejidad")
plt.plot(x,y)
plt.show()
# Ejecutar esto en trinket
#Resultados:
# y = 0.0119209289.., 9.674549..., 423660.87794...
# 4.- Cuales es el peor, promedio , y mejor tiempo
# Mejor tiempo: omega(1) se encuentra al primer intento
# Promedio: (pow(n,m)/2) -> pow(n,m) seria la mitad pero como se aplica tiempo asintotico nos quedamos pow(n,m)
# Peor: pow(n,m
# 5.- de haber mas contraseñas, cuales serian las complejidades?
# Serian las mismas porque no sabemos cuantas mas habrian