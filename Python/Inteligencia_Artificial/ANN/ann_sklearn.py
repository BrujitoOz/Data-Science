# Dataset
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
dataset = load_iris()
temp = train_test_split(dataset.data, dataset.target, test_size=0.2)
train_data,test_data,train_labels,test_labels=temp
# Preprocesamiento
from sklearn.preprocessing import StandardScaler
transformar = StandardScaler()
transformar.fit(train_data)
train_data = transformar.transform(train_data)
test_data=transformar.transform(test_data)
# Enrenamiento
from sklearn.neural_network import MLPClassifier
MultiCapa = MLPClassifier(hidden_layer_sizes = (10,10), activation='logistic', max_iter = 10000)
MultiCapa.fit(train_data, train_labels)
# Prediccion
predict = MultiCapa.predict(test_data)
print("Comparacion")
print(predict)
print(test_labels)
# Metricas de evaluacion
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report 
predictions_test = MultiCapa.predict(test_data)
print(accuracy_score(predictions_test, test_labels))
print(confusion_matrix(predictions_test, test_labels))
print(classification_report(predictions_test, test_labels))
# Graficando la perdida
plt.ylabel('Mean Square Error')
plt.xlabel('Epochs')
plt.plot(MultiCapa.loss_curve_)
plt.show()