import minisom
from sklearn import datasets
iris = datasets.load_iris()
iris_data = iris.data[:, :4]
iris_label = iris.target  
my_som = minisom.MiniSom(30, 30, 4, sigma=1.0, learning_rate=0.3)
my_som.train(iris_data, 100)
for i in range(len(iris_data)):
    coord = my_som.winner(iris_data[i])
    w1 = coord[0]
    w2 = coord[1]
    # iteracion   # coordenada ganadora       pesos de coordenada
    print(i, " ", coord, " ", my_som.get_weights()[w1][w2] )