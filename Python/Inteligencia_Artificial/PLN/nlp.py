#%% Dataset
import numpy as np
import pandas as pd
dataset = pd.read_csv("Restaurant_Reviews.tsv", delimiter="\t", quoting=3)
#%% Limpieza de texto
import re
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(0, 1000):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
#%% Bag of Words
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=1500)
x = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values
#%% Naive Bayes
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25, random_state = 0)
# Entrenamiento
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(x_train, y_train)
# Prediccion
y_pred = classifier.predict(x_test)
print(pd.DataFrame(y_pred, y_test))
# Matriz
from sklearn .metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)
# %%
