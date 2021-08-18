from IPython.display import Image
import tensorflow.keras
from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
model = ResNet50(weights='imagenet', include_top=True)
target_size=(224, 224)
print("Modelo cargado: {}".format(model.name))
img_path = 'test_image/cat.4001.jpg'
img = image.load_img(img_path, target_size=target_size)
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)
preds = model.predict(x)
print(decode_predictions(preds, top=10)[0])