
# type: ignore
from matplotlib import pyplot as plt
import numpy as np

alpha_pente = 3.7
longueur_pente = 31

alpha_plat = 0
longueur_plat = 10


g = 9.81



voitures_data = {
    'Dodge Charger': {
        'masse': 1760,
        'accélération': 5.1,
        'longueur': 5.28,
        'largeur': 1.95,
        'hauteur': 1.35,
        'cx': 0.38,
        'cz': 0.3,
        'mu': 0.1
    },
    'Toyota Supra': {
        'masse': 1615,
        'accélération': 5,
        'longueur': 4.51,
        'largeur': 1.81,
        'hauteur': 1.27,
        'cx': 0.29,
        'cz': 0.3,
        'mu': 0.1
    },
'Chevrolet Yenko': {
        'masse': 1498,
        'accélération': 5.3,
        'longueur': 4.72,
        'largeur': 1.88,
        'hauteur': 1.30,
        'cx': 0.35,
        'cz': 0.3,
        'mu': 0.1
    },
'Mazda RX-7': {
        'masse': 1385,
        'accélération': 5.2,
        'longueur': 4.3,
        'largeur': 1.88,
        'hauteur': 1.30,
        'cx': 0.35,
        'cz': 0.3,
        'mu': 0.1
    },
'Nissan Skyline': {
        'masse': 1540,
        'accélération': 5.8,
        'longueur': 4.6,
        'largeur': 1.79,
        'hauteur': 1.36,
        'cx': 0.34,
        'cz': 0.3,
        'mu': 0.1
    },

'Mitsubishi Lancer': {
        'masse': 1600,
        'accélération': 5,
        'longueur': 4.51,
        'largeur': 1.81,
        'hauteur': 1.48,
        'cx': 0.28,
        'cz': 0.3,
        'mu': 0.1
    },

}

voitures = list(voitures_data.keys())


def calcul_ligne_droite(voiture, alpha, longueur,vitesse=0):
    """
    Calcule le temps et la vitesse d'une voiture sur une pente.
    Args:
        voiture (dict): Un dictionnaire contenant les caractéristiques de la voiture.
            - 'mu' (float): Le coefficient de friction de la voiture.
            - 'accélération' (float): L'accélération de la voiture.
            - 'masse' (float): La masse de la voiture.
    Returns:
        tuple: Un tuple contenant:
            - temps (float): Le temps calculé pour la voiture sur la pente.
            - vitesse (float): La vitesse calculée de la voiture sur la pente.
    """
    # Calcul du temps en fonction de la gravité, de l'angle de la pente, du coefficient de friction et de l'accélération de la voiture
    temps = g * (np.sin(alpha) - (voiture['mu'] * np.cos(alpha))) + (voiture['accélération'] - (g * np.sin(alpha)) + (voiture['mu'] * g * np.cos(alpha)))

    # Ajustement du temps en fonction de la longueur de la pente
    temps = (2*longueur) / temps
    temps = np.sqrt(temps)

    # Calcul de la vitesse en fonction de la masse de la voiture, de la gravité, de l'angle de la pente, du coefficient de friction et de l'accélération
    vitesse = (voiture['masse'] * g * np.sin(alpha)) - (voiture['mu'] * voiture['masse'] * g * np.cos(alpha)) + (voiture['masse'] * (voiture['accélération'] - (g * np.sin(alpha)) + (voiture['mu'] * g * np.cos(alpha))))

    # Ajustement de la vitesse en fonction de la masse de la voiture
    vitesse = (1 / voiture['masse']) * vitesse

    # Ajustement de la vitesse en fonction du temps calculé
    vitesse = vitesse * temps

    # Retourne le temps et la vitesse calculés
    return temps, vitesse



def calcul_pente():

    for voiture in voitures:
        print(voiture,calcul_ligne_droite(voitures_data[voiture], alpha_pente, longueur_pente))
calcul_pente()

print("\n")

def calcul_pente():

    for voiture in voitures:
        print(voiture,calcul_ligne_droite(voitures_data[voiture], alpha_plat, longueur_plat))
calcul_pente()


def main(voiture):
    #1ère pente
    calcul_ligne_droite(voitures_data[voiture], alpha_pente, longueur_pente)

    #2nd plat après looping
    calcul_ligne_droite(voitures_data[voiture], alpha_plat, longueur_plat)
