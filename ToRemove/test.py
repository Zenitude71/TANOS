def create_files(n):
    for i in range(1, n + 1):
        filename = f"./ToRemove/fichier({i}).txt"
        with open(filename, 'w') as file:
            file.write(f"Contenu du fichier {i}\n")

# Exemple d'utilisation
n = 10  # Remplacez 10 par le nombre de fichiers que vous voulez créer
create_files(n)