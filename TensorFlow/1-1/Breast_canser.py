import numpy as np
import codecs
import csv

with codecs.open('Breast_Canser.csv','r','utf-8') as f:
    dataSet = np.array([row for row in csv.reader(f)][1 :])
    
X = dataSet[:,2:]
Y = dataSet[:,1]

Y_converte = {w:i for i,w in enumerate(sorted(set(Y)))}
Y = np.array(list(map(lambda x : Y_converte[x],Y)))
print(type(X))