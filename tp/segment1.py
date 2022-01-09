
import numpy as np
import matplotlib.pyplot as plt
import tensorflow.keras as keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD

input = np.genfromtxt('inputs.csv', delimiter=",")
output = np.genfromtxt('output.csv', delimiter=",")
output = keras.utils.to_categorical(output)

sgd = SGD(lr= 0.1)
model = Sequential()
model.add(Dense(10, input_dim=7, activation='softmax'))
model.summary()
model.compile(optimizer=sgd, loss='categorical_crossentropy')
history = model.fit(input,output, epochs=10000)

plt.plot(history.history['loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.show()

value_to_guess = np.array([[1,1,1,1,1,1,1], [0,1,1,0,0,0,0], [0,0,1,0,0,0,0]])
predictions = model.predict(value_to_guess)
print(str(np.argmax(predictions, axis=-1)))