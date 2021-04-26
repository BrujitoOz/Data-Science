# In[1]:
import random
import math
# ### Clase Ciudad
# In[2]:
class Ciudad:
    def __init__(self, lon, lat, name):
        self.lon = lon
        self.lat = lat
        self.name = name

    def distancia(self, ciudad):
        distanciaX = (ciudad.lon - self.lon) * 40000 * math.cos((self.lat + ciudad.lat) * math.pi / 360) / 360
        distanciaY = (self.lat - ciudad.lat) * 40000 / 360
        distancia = math.sqrt((distanciaX * distanciaX) + (distanciaY * distanciaY))
        return distancia

    def get_nombre_ciudad(ciudad):
        return ciudad.name
# ### Clase administrción de tour
# In[3]:
class TourAdmin:
    destino_ciudades = []
    def add_city(self, ciudad):
        self.destino_ciudades.append(ciudad)
    def get_city(self, index):
        return self.destino_ciudades[index]
    def numero_de_ciudades(self):
        return len(self.destino_ciudades)
# ### clase tour
# In[4]:
class Tour:
    def __init__(self, tour_admin, tour=None):
        self.tour_admin = tour_admin
        self.tour = []
        self.distancia = 0
        if tour is not None:
            self.tour = list(tour)
        else:
            for i in range(0, self.tour_admin.numero_de_ciudades()):
                self.tour.append(None)

    def __getitem__(self, index):
        return self.tour[index]

    def generar_tour(self):
        for indice_ciudad in range(0, self.tour_admin.numero_de_ciudades()):
            self.set_city(indice_ciudad, self.tour_admin.get_city(indice_ciudad))
        #random.shuffle(self.tour)

    def get_city(self, tour_position):
        return self.tour[tour_position]

    def set_city(self, tour_position, ciudad):
        self.tour[tour_position] = ciudad
        self.distancia = 0

    def get_distancia(self):
        if self.distancia == 0:
            tour_distancia = 0
            for indice_ciudad in range(0, self.tour_tam()):
                ciudad_inicio = self.get_city(indice_ciudad)
                if indice_ciudad + 1 < self.tour_tam():
                    ciudad_llegada = self.get_city(indice_ciudad + 1)
                else:
                    ciudad_llegada = self.get_city(0)
                tour_distancia += ciudad_inicio.distancia(ciudad_llegada)
            self.distancia = tour_distancia

        return self.distancia

    def tour_tam(self):
        return len(self.tour)

    def mostrar(self):
        for i in range(0, self.tour_tam()):
            print(Ciudad.get_nombre_ciudad(self.get_city(i)))
# ### Simulated Annealing
# In[5]:
class SimulatedAnnealing:
    def __init__(self, destinos, temperatura_inicial, velocidad_enfriamiento):
        self.tour_admin = destinos
        self.tour = Tour(destinos)
        self.tour.generar_tour()
        self.el_mejor = self.tour
        self.temperatura = temperatura_inicial
        self.velocidad_enfriamiento = velocidad_enfriamiento
        self.cont =0

    def funcion_aceptacion(self, delta_energia):
        if delta_energia < 0:
            return True
        elif random.random() <= math.exp(-(delta_energia / self.temperatura)):
            return True
        return False

    def nuevo_tour(self):
        tour_nuevo = Tour(self.tour_admin, self.tour)
        pos1 = random.randrange(self.tour.tour_tam())
        pos2 = random.randrange(self.tour.tour_tam())
        ciudad1 = tour_nuevo.get_city(pos1)
        ciudad2 = tour_nuevo.get_city(pos2)
        tour_nuevo.set_city(pos2, ciudad1)
        tour_nuevo.set_city(pos1, ciudad2)

        actual_energia = self.tour.get_distancia()
        nueva_energia = tour_nuevo.get_distancia()
        delta = nueva_energia - actual_energia
        if self.funcion_aceptacion(delta):
            self.tour = tour_nuevo
        if tour_nuevo.get_distancia() < self.el_mejor.get_distancia():
            self.el_mejor = tour_nuevo
            print(tour_nuevo.get_distancia())

    def run(self):
        while self.temperatura > 1:
            self.cont = self.cont+1
            self.nuevo_tour()
            self.temperatura *= 1 - self.velocidad_enfriamiento
# ### Función de integración
# In[6]:
destinos = TourAdmin()
ciudad1 = Ciudad(-77.0282400, -12.0431800, 'Lima')
destinos.add_city(ciudad1)

ciudad2 = Ciudad(-55.0000000, -10.0000000, 'Brasil')
destinos.add_city(ciudad2)
ciudad3 = Ciudad(-65.0000000, -17.0000000, 'Bolivia')
destinos.add_city(ciudad3)
ciudad4 = Ciudad(-58.0000000, -23.0000000, 'Paraguay')
destinos.add_city(ciudad4)
ciudad5 = Ciudad(-71.0000000, -30.0000000, 'Chile')
destinos.add_city(ciudad5)

sa = SimulatedAnnealing(destinos, temperatura_inicial=10000, velocidad_enfriamiento=0.003)
print(sa.tour.mostrar())
print(sa.tour.get_distancia())
sa.run()

print(sa.tour.mostrar())
print(sa.tour.get_distancia())
print(sa.cont)