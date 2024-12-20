
# type: ignore
from matplotlib import pyplot as plt
import numpy as np

afficher_graphique = True

alpha_pente = 3.7
longueur_pente = 31

hauteur_ravin = 1
longueur_ravin = 9 

longueur_plat = 6

longueur_sprint = 10

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


def calcul_ligne_droite(voiture, longueur,alpha=0,vitesse_i=0):
    
    acceleration = voiture["accélération"]


    delta = 0.001
    k = 0.5 * 1.3 * voiture["hauteur"] * voiture["largeur"] * voiture["cx"]
    x=0
    temps = 0
    vitesse = vitesse_i

    while x<longueur:
        vitesse = ((g * np.sin(np.radians(alpha))) + acceleration - ((voiture["mu"]*g*np.cos(np.radians(alpha)))) - ((k * (vitesse ** 2)) / voiture["masse"])) * delta + vitesse
        x = 0.5 * ((g * np.sin(np.radians(alpha))) + acceleration - ((voiture["mu"]*g*np.cos(np.radians(alpha)))) - ((k * (vitesse ** 2)) / voiture["masse"])) * (delta ** 2) + (vitesse * delta) + x
        temps += delta
    return temps, vitesse


def looping(voiture, rayon, vitesse_i):
    
    acceleration = voiture["accélération"]
    delta = 0.001
    w = vitesse_i / rayon
    print(vitesse_i)
    theta = -np.pi/2
    temps = 0
    k = 0.5 * 1.3 * voiture["hauteur"] * voiture["largeur"] * voiture["cx"]
    liste_x = []
    liste_y = []

    liste_x.append(0)
    liste_y.append(w)

    while theta < 2 * np.pi:
        w = (((acceleration) - (g * np.sin(theta)) - (voiture["mu"] * g * np.cos(theta)) - ((k/voiture["masse"]) + (rayon * voiture["mu"]))* w ** 2)/rayon * delta + w) 
        theta = (((acceleration) - (g * np.sin(theta)) - (voiture["mu"] * g * np.cos(theta)) - ((k/voiture["masse"]) + (rayon * voiture["mu"])) * w ** 2)/rayon) * ((delta ** 2)/2) +( w * delta) + theta
        temps += delta

        liste_x.append(temps)
        liste_y.append(w)
    if afficher_graphique:
        plt.plot(liste_x, liste_y)
        plt.xlabel('Temps (s)')
        plt.ylabel('Vitesse angulaire (deg/s)')
        plt.title(f'Vitesse angulaire en fonction du temps de la voiture {nom}')
        plt.grid(True)
        plt.show()

    print(w*rayon)

    return temps, w* rayon


def ravin(voiture,vitesse_initiale):
    écart_temps = 0.001
    k_x = 0.5 * 1.3 * voiture['cx'] * voiture['largeur'] * voiture['hauteur']
    k_y = 0.5 * 1.3 * voiture['cz'] * voiture['largeur'] * voiture['longueur']

    liste_x = []
    liste_y = []

    x = 0
    y = hauteur_ravin 

    v_x = vitesse_initiale
    v_y = 0

    liste_x.append(x)
    liste_y.append(y)
    x_moins_1 = 0
    y_moins_1 = hauteur_ravin
    while y >= 0:
        
        v_x = ((-k_x * (v_x ** 2))/voiture['masse']) * écart_temps + v_x
        x = 0.5 * ((-k_x * (v_x ** 2))/voiture['masse']) * (écart_temps ** 2) +(v_x * écart_temps) + x

        
        v_y = ((-g) + ((k_y * (v_y ** 2))/voiture['masse'])) * écart_temps + v_y
        y = 0.5*((-g) + (k_y * (v_y ** 2))/voiture['masse']) * (écart_temps ** 2) + v_y * écart_temps + y        

        liste_x.append(x)
        liste_y.append(y)
    if afficher_graphique:
        plt.plot(liste_x, liste_y)
        plt.xlabel('Distance (m)')
        plt.ylabel('Hauteur (m)')
        plt.title(f'Trajectoire de la voiture{nom}')
        plt.grid(True)
        plt.show()
    return len(liste_x) * écart_temps, v_x, x

def main(voiture_nom,):


    temps = 0
    #1ère pente
    calcul = calcul_ligne_droite(voitures_data[voiture_nom], alpha=alpha_pente, longueur=longueur_pente)
    temps += calcul[0]
    vitesse = calcul[1]

    #Looping
    calcul = looping(voitures_data[voiture_nom], rayon=6, vitesse_i=vitesse)
    temps += calcul[0]
    vitesse = calcul[1]

    #Ravin
    calcul = ravin(voitures_data[voiture_nom],vitesse)
    temps += calcul[0]
    vitesse = calcul[1]
    longueur_saut = calcul[2]
    if longueur_saut < longueur_ravin:
        return 0

    #Sprint final
    calcul = calcul_ligne_droite(voitures_data[voiture_nom], longueur=longueur_sprint,vitesse_i=vitesse)
    temps += calcul[0]
    vitesse = calcul[1]


    return temps, vitesse





def globale():
    afficher_graphique = False
    for voiture in voitures:
        global nom
        nom = voiture
        res = main(voiture)
        if res == 0:
            print(f"La voiture {voiture} n'a pas réussi à sauter le ravin")
        else:
            print(f"La voiture {voiture} a mis {round(res[0],1)} secondes pour parcourir le circuit et a atteint une vitesse de {round(res[1],1)} m/s")

globale()