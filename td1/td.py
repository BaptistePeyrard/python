# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from character import Character
from Army import Army
import csv
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

#Liste contenant les objets Character
characters_list = np.array([])
#On ouvre le fichier csv
with open('characters.csv', newline='') as csvfile:
    liste_personnage = csv.DictReader(csvfile)
    #Pour chaque ligne du csv, on crée un objet Character et on l'ajoute au tableau
    for row in liste_personnage:
        c = Character(row['name'], row['first name'], row['age'], row['profession'], row['morale value'])
        characters_list = np.append(characters_list, c)

#Creation de deux tableaux pour stocker le morale initial et le boost du chef de chaque armée
moral_list = np.array([])
boost_list = np.array([])
#On parcourt la liste des Characters
for personnage in characters_list:
    #Pour chaque character, on créer une armée et on ajoute son morale et son boost
    a = Army(personnage)
    print(a)
    moral_list = np.append(moral_list, a.getMoral())
    boost_list = np.append(boost_list, personnage.getBoost_de_moral())
#On crée un tableau contenant la somme de chaque ligne des deux tableaux
somme = moral_list*boost_list
#On affiche les valeurs avec 1 decimale
print(round(np.sum(somme),1))


#On crée les tableaux input et output
and_input = [[0, 0, 1, 1], [0, 1, 0, 1]]
and_output = [0, 0, 0, 1]
#On crée une liste de dimension 10x10 pour chaque cas possible afin de stocker les valeurs d'erreur pour chaque combinaison de poids
liste_0 = np.double([[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10]])
liste_1 = np.double([[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10]])
liste_2 = np.double([[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10]])
liste_3 = np.double([[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10]])
#On parcourt chaque combinaisons de poids
for w1 in range(-5,6):
    for w2 in range(-5,6):
        #Pour chaque cas possible :
        for i in range(0,4):
            calcul = w1 * float(and_input[0][i]) + w2 * float(and_input[1][i])
            t = and_output[i]
            if calcul <= 0:
                y = 0
            else:
                y = 1
            if i == 0:
                liste_0[w1 + 5][w2 + 5] = 0.5 * (y - t) ** 2
            elif i == 1:
                liste_1[w1 + 5][w2 + 5] = 0.5 * (y - t) ** 2
            elif i == 2:
                liste_2[w1 + 5][w2 + 5] = 0.5 * (y - t) ** 2
            else:
                liste_3[w1 + 5][w2 + 5] = 0.5 * (y - t) ** 2
#On fait la somme de toutes les listes
liste_final = liste_0 + liste_1 + liste_2 + liste_3
print("")
print(liste_final)
#Affichage
fig = plt.figure()
fig = fig.add_subplot(121)
fig.imshow(liste_final, interpolation='nearest', cmap=cm.Greys_r)
plt.show()
