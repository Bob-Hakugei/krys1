import os

# Fonction pour envoyer des commandes à l'ordinateur
def envoyer_commande(commande):
    os.system(commande)

# Boucle principale du programme
while True:
    # Attendre l'entrée de l'utilisateur
    commande_utilisateur = input("Entrez une commande : ")

    # Envoyer la commande à l'ordinateur via Termux
    envoyer_commande(commande_utilisateur)
