import random

from character import Character

class Army:
    #Constructeur
    def __init__(self, chef):
        self.chef = chef
        #Fonction random pour la valeur de morale initiale
        self.moral = round(random.uniform(20,100),1)

    #Surcharge de la méthode __repr__ pour personnalisé notre affichage des armées
    def __repr__(self):
        return "Armée de " +self.chef.getPrenom() + " " + self.chef.getNom() + " Moral initial : " + str(self.moral) + ", Boost du chef : " + str(self.getChef().getBoost_de_moral()) + ", Moral total : " + str(self.get_total_moral())

    def getChef(self):
        return self.chef
    def getMoral(self):
        return self.moral

    def setChef(self, chef):
        self.chef = chef
    def setMoral(self, moral):
        self.moral = moral

    def get_total_moral(self):
        return round(float(self.chef.getBoost_de_moral())*float(self.moral),1)