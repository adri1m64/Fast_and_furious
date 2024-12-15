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
    
    # Calcul de la résistance sur la pente
    res = g * (np.sin(alpha) - (voiture['mu'] * np.cos(alpha)))
    # Calcul de la résistance due à l'accélération de la voiture
    res2 = voiture['accélération'] - (g * np.sin(alpha)) + (voiture['mu'] * g * np.cos(alpha))
    # Addition des deux résistances
    res = res + res2
    # Calcul du temps en fonction de la résistance totale
    res = (2*longueur) / res
    res = np.sqrt(res)
    temps = res

    # Calcul de la force de traction sur la pente
    res3 = (voiture['masse'] * g * np.sin(alpha)) - (voiture['mu'] * voiture['masse'] * g * np.cos(alpha))
    # Calcul de la force due à l'accélération de la voiture
    res4 = voiture['masse'] * (voiture['accélération'] - (g * np.sin(alpha)) + (voiture['mu'] * g * np.cos(alpha)))
    # Addition des deux forces
    res3 = res3 + res4
    # Calcul de l'accélération totale
    res3 = (1 / voiture['masse']) * res3
    # Calcul de la vitesse en fonction de l'accélération totale et du temps
    res3 = res3 * temps
    vitesse = res3

    return res, vitesse



def calcul_pente():

    for voiture in voitures:
        print(voiture,calcul_ligne_droite(voitures_data[voiture], alpha_pente, longueur_pente))
calcul_pente()

print("\n")

def calcul_pente():

    for voiture in voitures:
        print(voiture,calcul_ligne_droite(voitures_data[voiture], alpha_plat, longueur_plat))
calcul_pente()
