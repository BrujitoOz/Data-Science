import numpy as np
import random
import re
import os
from PIL import Image
# matrix to vector
def mat2vec(x):
    m = x.shape[0] * x.shape[1]
    tmp1 = np.zeros(m)
    c = 0
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            tmp1[c] = x[i, j]
            c += 1
    return tmp1

# creamos matrix n x n y entrenamos
def create_w(x):
    if len(x.shape) != 1:
        print("No es un vector")
        return
    else:
        w = np.zeros([len(x), len(x)])
        for i in range(len(x)):
            for j in range(i, len(x)):
                if i == j:
                    w[i, j] = 0
                else:
                    w[i, j] = x[i] * x[j]
                    w[j, i] = w[i, j]
    return w
# leemos la imagen y la convertimos en array
def readimg2array(file, size, threshold = 145):
    pilimg = Image.open(file).convert(mode="L")
    pilimg = pilimg.resize(size)
    imgarray = np.asarray(pilimg, dtype=np.uint8)
    x = np.zeros(imgarray.shape, dtype = np.float64)
    x[imgarray > threshold] = 1
    x[x == 0] = -1
    return x
def array2img(data, outfile = None):
    y = np.zeros(data.shape, dtype = np.uint8)
    y[data == 1] = 255
    y[data == -1] = 0
    img = Image.fromarray(y, mode= "L")
    if outfile is not None:
        img.save(outfile)
    return img
# funcion de activacion
def funcionactivacion(w, y_vec, theta = 0.5, time = 100):
    for s in range(time):
        m = len(y_vec)
        i = random.randint(0, m - 1)
        u = np.dot(w[i][:], y_vec) - theta
        if u > 0:
            y_vec[i] = 1
        elif u < 0:
            y_vec[i] = -1
    return y_vec
# algoritmo hopfield
def hopfield(train_files, test_files, theta = 0.5, time = 100, size = (100,100), threshold = 145, current_path = None):
    print("Importando archivos")
    num_files = 0
    for path in train_files:
        x = readimg2array(file = path, size = size, threshold = threshold)
        x_vec = mat2vec(x)
        if num_files == 0:
            w = create_w(x_vec)
            num_files = 1
        else:
            tmp_w = create_w(x_vec)
            w = w + tmp_w
            num_files += 1
    # prueba
    counter = 0
    for path in test_files:
        y = readimg2array(file=path, size=size, threshold=threshold)
        oshape = y.shape
        # y_img = array2img(y)
        y_vec = mat2vec(y)
        y_vec_after = funcionactivacion(w=w, y_vec= y_vec, theta= theta, time=time)
        y_vec_after = y_vec_after.reshape(oshape)

        if current_path is not None:
            outfile = current_path + "/after_" + str(counter) + ".jpg"
            array2img(y_vec_after, outfile= outfile)
            salida = array2img(y_vec_after, outfile=outfile)
            salida.show()
        else:
            salida = array2img(y_vec_after, outfile= None)
            salida.show()
        counter += 1
        print("FIN")

# Funcion principal 
# para archivos de entrenamiento
current_path = os.getcwd()
train_paths = []
path = current_path + "/train_pics1/"
for i in os.listdir(path):
  train_paths.append(path+i)

# para archivos de prueba
test_paths = []
path = current_path + "/test_pics1/"
for i in os.listdir(path):
  test_paths.append(path+i)


# invocando a la funcion hopfield
hopfield(train_files=train_paths, test_files=test_paths, theta=0.5, time=100, size = (100, 100), threshold=145, current_path=current_path )