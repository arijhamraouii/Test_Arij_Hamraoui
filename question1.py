# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 13:57:45 2025

@author: arijh
"""

# Fonction pour calculer la somme des valeurs d'étalonnage dans un fichier
def extraire_somme_etalonnage(chemin_fichier):
    # Initialiser la somme des valeurs d'étalonnage
    somme_etalonnage = 0

    # Ouvrir le fichier en mode lecture
    with open(chemin_fichier, 'r') as fichier:
        # Initialiser le compteur de ligne
        index = 1
        # Parcourir chaque ligne du fichier
        for ligne in fichier:
            # Supprimer les espaces ou sauts de ligne inutiles
            ligne = ligne.strip()
            premier_chiffre = ''  # Variable pour stocker le premier chiffre trouvé
            dernier_chiffre = ''  # Variable pour stocker le dernier chiffre trouvé

            # Parcourir chaque caractère de la ligne pour trouver le premier chiffre
            for char in ligne:
                if char.isdigit():
                    premier_chiffre = char
                    break  # Arrêter dès que le premier chiffre est trouvé

            # Parcourir la ligne à l'envers pour trouver le dernier chiffre
            for char in reversed(ligne):
                if char.isdigit():
                    dernier_chiffre = char
                    break  # Arrêter dès que le dernier chiffre est trouvé

            # Si au moins un chiffre est trouvé, former le nombre à partir des chiffres
            if premier_chiffre or dernier_chiffre:
                nombre_forme = int(premier_chiffre + dernier_chiffre)
                # Afficher la concaténation des chiffres trouvés pour chaque ligne
                print(f"Ligne {index}: {premier_chiffre}{dernier_chiffre}")
                # Ajouter le nombre formé à la somme totale
                somme_etalonnage += nombre_forme
            else:
                print(f"Ligne {index}: Aucun chiffre trouvé")  # Afficher si aucun chiffre n'est trouvé

            # Incrémenter le compteur de ligne
            index += 1

    # Afficher la somme totale des valeurs d'étalonnage
    print(f"\nLa somme des valeurs d'étalonnage est : {somme_etalonnage}")

# Définir le chemin du fichier contenant les données
chemin_fichier = "C:/Users/arijh/Desktop/Test_Arij_Hamraoui/document.txt"

# Appeler la fonction pour calculer et afficher la somme des valeurs d'étalonnage
extraire_somme_etalonnage(chemin_fichier)
