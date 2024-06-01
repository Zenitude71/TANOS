import os
import re

def lister_doublons(dossier):
    # Expression régulière pour détecter les fichiers doublons
    pattern = re.compile(r'^(.*)\((\d+)\)(\.[^.]+)$')
    
    # Dictionnaire pour stocker les noms de fichiers originaux
    fichiers_originaux = set()
    fichiers_doublons = []

    for nom_fichier in os.listdir(dossier):
        chemin_complet = os.path.join(dossier, nom_fichier)
        
        # Vérifier si c'est un fichier
        if os.path.isfile(chemin_complet):
            # Chercher un match avec le pattern des fichiers doublons
            match = pattern.match(nom_fichier)
            if match:
                nom_base = match.group(1).strip()
                extension = match.group(3)
                nom_original = f"{nom_base}{extension}"

                # Vérifier si le fichier original existe
                if nom_original in fichiers_originaux or os.path.exists(os.path.join(dossier, nom_original)):
                    fichiers_doublons.append(chemin_complet)
                else:
                    # Ajouter le nom original à l'ensemble pour référence future
                    fichiers_originaux.add(nom_original)
            else:
                # Ajouter le nom de fichier à l'ensemble des fichiers originaux
                fichiers_originaux.add(nom_fichier)
    
    return fichiers_doublons


def supprimer_fichiers(fichiers_doublons):
    for fichier in fichiers_doublons:
        print(f"Suppression du doublon: {fichier}")
        os.remove(fichier)