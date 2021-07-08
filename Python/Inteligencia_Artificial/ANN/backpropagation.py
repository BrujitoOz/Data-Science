import numpy as np
def sigmoid(x):
  return 1/(1 + np.exp(-x))
def sigmoid_derivative(x):
  return x*(1-x)
inputs = np.array([
  [0,0],
  [1,0],
  [0,1],
  [1,1]
  ])
expected_output = np.array([
  [0],
  [1],
  [1],
  [0]
  ])
epochs = 5000
lr = 0.25
inputLayerNeurons, hiddenLayerNeurons, outputLayerNeurons = 2, 2, 1 

hidden_weights = np.random.uniform(size=(inputLayerNeurons,hiddenLayerNeurons))
hidden_bias = np.random.uniform(size=(1,hiddenLayerNeurons))

output_weights = np.random.uniform(size=(hiddenLayerNeurons,outputLayerNeurons))
output_bias = np.random.uniform(size=(1,outputLayerNeurons))


hidden_weights[0][0] = 0.100
hidden_weights[0][1] = -0.700

hidden_weights[1][0] = 0.500
hidden_weights[1][1] = 0.300

output_weights[0] = 0.200
output_weights[1] = 0.400

for _ in range(epochs):
  # Propagación hacia adelante
  hidden_layer_activation = np.dot(inputs,hidden_weights )
  hidden_layer_activation += hidden_bias
  hidden_layer_output = sigmoid(hidden_layer_activation)

  output_layer_activation = np.dot(hidden_layer_output, output_weights)
  output_layer_activation += output_bias
  predicted_output = sigmoid(output_layer_activation)

  # Propagación hacia atras
  error = expected_output - predicted_output
  d_predicted_output = error * sigmoid_derivative(predicted_output)

  error_hidden_layer = d_predicted_output.dot(output_weights.T)
  d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)

  # Actualizando los pesos
  output_weights += hidden_layer_output.T.dot(d_predicted_output) * lr 
  #output_bias += np.sum(d_predicted_output) * lr

  hidden_weights += inputs.T.dot(d_hidden_layer) * lr
  #hidden_bias += np.sum(d_hidden_layer) * lr
print("Pesos finales de la capa oculta")
print(hidden_weights)
print("Pesos finales de la capa de salida")
print(output_weights)
print("Predicción")
print(predicted_output)