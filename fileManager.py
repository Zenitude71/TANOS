import os
import re
from send2trash import send2trash

def lister_doublons(dossier, recursive=False):
    # Expression régulière pour détecter les fichiers doublons
    pattern = re.compile(r'^(.*)\((\d+)\)(\.[^.]+)$')
    
    # Dictionnaire pour stocker les noms de fichiers originaux
    fichiers_originaux = set()
    fichiers_doublons = []

    for root, dirs, files in os.walk(dossier):
        for nom_fichier in files:
            chemin_complet = os.path.normpath(os.path.join(root, nom_fichier))
            
            # Chercher un match avec le pattern des fichiers doublons
            match = pattern.match(nom_fichier)
            if match:
                nom_base = match.group(1).strip()
                extension = match.group(3)
                nom_original = os.path.normpath(os.path.join(root, f"{nom_base}{extension}"))

                # Vérifier si le fichier original existe
                if nom_original in fichiers_originaux or os.path.exists(nom_original):
                    fichiers_doublons.append(chemin_complet)
                else:
                    # Ajouter le nom original à l'ensemble pour référence future
                    fichiers_originaux.add(nom_original)
            else:
                # Ajouter le nom de fichier à l'ensemble des fichiers originaux
                fichiers_originaux.add(nom_fichier)
        
        if not recursive:
            break
    
    return fichiers_doublons

def supprimer_fichiers(fichiers_doublons):
    for fichier in fichiers_doublons:
        print(f"Suppression du doublon: {fichier}")
        os.remove(fichier)

def envoyer_a_la_corbeille(fichiers_doublons):
    for fichier in fichiers_doublons:
        print(f"Envoi à la corbeille: {fichier}")
        send2trash(fichier)
