import numpy as np
import csv
from Perceptron import Perceptron

#Creation d'un objet Perceptron
perceptron_and = Perceptron(4, 100, 0.01)

inputs = np.array([[0,0],[0,1],[1,0],[1,1]])
outputs = np.array([0,0,0,1])

perceptron_and.train(inputs, outputs)


with open('poids.csv', 'w', newline='') as csvfile:
    fieldnames = ['w0', 'w1', 'w2']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'w0': perceptron_and.get_w0(), 'w1': perceptron_and.get_w1(), 'w2': perceptron_and.get_w2()})

