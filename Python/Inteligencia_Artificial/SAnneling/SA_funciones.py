import random, math
class SA:
    def __init__(self, current, best, new, temperatura, vel_enfriamiento):
        self.current = current
        self.best = best
        self.new = new
        self.temperatura = temperatura
        self.vel_enfriamiento = vel_enfriamiento

    # Calcula energia
    def fun(self, x):
        x = self.decimal_binario(int(x))
        return x**3-60*x**2+900*x+100

    def Aleatorio(self):
        return random.randint(1,5)

    def Reemplazar(self, i, new):
        l = list(new)
        if l[i-1] == '0':
            l[i-1] = '1'
        elif l[i-1] == '1':
            l[i-1] = '0'
        new = ''.join(str(i) for i in l)
        return new 
            
    # Convertidores
    def decimal_binario(self, x):
        return int(str(x), 2)

    def FAceptacion(self, current, new, temperatura):
      ecurrent = self.fun(current)
      enew = self.fun(new)
      if enew < ecurrent:
        prob = 1
      else:
        prob = math.exp((ecurrent-enew)/temperatura)
      if prob > random.random():
        current = new
      return current

    def BestSol(self, current, best):
      ebest = self.fun(best)
      ecurrent = self.fun(current)
      if ecurrent > ebest:
        best = current
        print("binario:", best)
        print("decimal:", self.decimal_binario(best))
        print("energia:", self.fun(best))

      return best

    def UpdateTemp(self, temperatura, vel_enfriamiento):
      temp = (1-vel_enfriamiento)*temperatura
      return temp
    
    def sol(self):
        # Inicio
        print("estado inicio:", self.current)
        print("decimal:", self.decimal_binario(best))
        print("energia:", self.fun(best))
        print()
        while self.temperatura > 1:
          # Reemplazo aleatorio
          aleatorio = self.Aleatorio()
          self.new = self.Reemplazar(aleatorio, self.new)
          
          self.current = self.FAceptacion(self.current, self.new, self.temperatura )

          self.best = self.BestSol(self.current, self.best)
          
          self.temperatura = self.UpdateTemp(self.temperatura, self.vel_enfriamiento)

current = "10011"
best = current
new = current

IA = SA(current, best, new, 1000, 0.045)
IA.sol()