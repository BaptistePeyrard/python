class Character:
    #Constructeur
    def __init__(self, nom, prenom, age, profession, boost_de_moral):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.profession = profession
        self.boost_de_moral = boost_de_moral

    # Surcharge de la méthode __repr__ pour personnalisé notre affichage des armées
    def __repr__(self):
        return self.prenom + " " + self.nom + ", he/she is " + self.age \
               + " years old, he/she is a " + self.profession \
               + " and he/she has a morale boost of " + self.boost_de_moral

    def getNom(self):
        return self.nom
    def getPrenom(self):
        return self.prenom
    def getAge(self):
        return self.age
    def getProfession(self):
        return self.profession
    def getBoost_de_moral( self ) :
        return float(self.boost_de_moral)

    def setNom(self, nom):
        self.nom = nom
    def setPrenom(self, prenom):
        self.prenom = prenom
    def setAge(self, age):
        self.age = age
    def setProfession(self, profession):
        self.profession = profession
    def setBoost_de_moral(self, boost_de_moral):
        self.boost_de_moral = boost_de_moral
