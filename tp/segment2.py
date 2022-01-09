
import csv
import numpy as np
import tensorflow.keras as ke
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD

#input = np.array([1,1,1,1,1,1,0],[0,1,1,0,0,0,0],[1,1,0,1,1,0,1],[1,1,1,1,0,0,1],[0,1,1,0,1,1,1],[1,0,1,1,0,1,1],[1,0,1,1,1,1,1],[1,1,1,0,0,1,0],[1,1,1,1,1,1,1],[1,1,1,1,0,1,1])
#output = np.array([0,1,2,3,4,5,6,7,8,9])


input = np.genfromtxt('inputs.csv', delimiter=",")
output = np.genfromtxt('output.csv', delimiter=",")
print(output)
output = ke.utils.to_categorical(output)
print(output)

sgd = SGD(lr=10)
model = Sequential()
model.add(Dense(10, input_dim=7, activation='softmax'))
model.summary()
model.compile(optimizer=sgd, loss='mean_squared_error')
model.fit(input,output, epochs=2000)

value_to_guess = np.array([[1,1,1,1,1,1,0], [0,1,1,0,0,0,0], [1,1,1,1,0,1,0]])
predictions = model.predict(value_to_guess)
for v in predictions:
    print(str(round(v[0])) + " " + str(round(v[1])) + " " + str(round(v[2])) + " " + str(round(v[3])) + " " + str(round(v[4])) + " " + str(round(v[5])) + " " + str(round(v[6])) + " " + str(round(v[7])) + " " + str(round(v[8])) + " " + str(round(v[9])))