

class Perceptron :

    #Constructeur du perceptron avec son nombre d'inputs, d'epochs, ses poids et son learning rate
    def __init__(self, nbr_input, nbr_epoch, learning_rate):
        self.nbr_input = nbr_input
        self.nbr_epoch = nbr_epoch
        self.learning_rate = learning_rate
        self.w0 = 0
        self.w1 = 0
        self.w2 = 0

    #La fonction predict renvoie la sortie du perceptron pour un tableau d'input donné
    def predict(self, input1, input2):
        resultat = self.w1 * input1 + self.w2 * input2 + self.w0 * 1
        if resultat > 0:
            resultat = 1
        else:
            resultat = 0
        return resultat

    #La fonction train va analyser les résultats des input par rapport aux outputs attendus et corriger les poids en fonction
    def train(self, inputs, outputs):
        #compteur va contenir le numéro de la boucle d'apprentissage
        compteur = 0
        #compteur_val_erreur va contenir le nombre de valeurs d'erreur egales successives
        compteur_val_erreur = 0
        #save_erreur va garder en mémoire
        save_erreur = 100
        while compteur < self.nbr_epoch :
            valeurs = "Valeurs : "
            erreur = 0
            #On parcourt tous les input
            for i in range(0, len(inputs)) :
                #Pour chaque input, on prédit la sortie et on ajuste les poids en fonction
                sortie_obs = self.predict(inputs[i][0], inputs[i][1])
                valeurs += str(sortie_obs) + " ; "
                self.w0 = self.w0 + self.learning_rate * (outputs[i] - sortie_obs) * 1
                self.w1 = self.w1 + self.learning_rate * (outputs[i] - sortie_obs) * inputs[i][0]
                self.w2 = self.w2 + self.learning_rate * (outputs[i] - sortie_obs) * inputs[i][1]
                #calcul de la valeur d'erreur
                erreur += 0.5 * (sortie_obs - outputs[i]) ** 2
            compteur += 1
            if save_erreur == erreur :
                compteur_val_erreur += 1
            else:
                compteur_val_erreur = 0
            save_erreur = erreur

            #Affichage
            print("Test numéro : " + str(compteur))
            print(valeurs)
            print("Valeurs des poids :  " + str(self.w0) + " " + str(self.w1) + " " + str(self.w2))
            print("Valeur d'erreur :" + str(erreur) + "\n")

            if compteur_val_erreur == 4 :
                compteur = self.nbr_epoch

    def get_w0(self):
        return self.w0

    def get_w1(self):
        return self.w1

    def get_w2(self):
        return self.w2
