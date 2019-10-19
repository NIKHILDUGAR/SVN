import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib

dataset = pd.read_csv("D:\\MLH Project\\datasets\\dataset.csv")
#dataset = dataset.drop('id', 1)
x = dataset.iloc[ : , :-1].values
y = dataset.iloc[:, -1:].values
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.25, random_state =0 ) 
classifier = LogisticRegression(random_state = 0)
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)
joblib.dump(classifier, 'Model\\logisticReg_final.pkl')