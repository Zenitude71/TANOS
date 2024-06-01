import os
import re
from fileManager import *
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QFileDialog, QMessageBox

# Classe principale de la fenêtre
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TANOS")
        
        # Définir la taille minimale de la fenêtre
        self.setMinimumSize(400, 200)
        
        self.layout = QVBoxLayout()

        # Zone de texte pour afficher le chemin du dossier sélectionné
        self.path_text = QLineEdit(self)
        self.layout.addWidget(self.path_text)

        # Bouton pour ouvrir le dialogue de sélection de dossier
        self.select_button = QPushButton("Sélectionner le dossier", self)
        self.select_button.clicked.connect(self.select_folder)
        self.layout.addWidget(self.select_button)

        # Bouton pour supprimer les doublons
        self.delete_button = QPushButton("Supprimer les doublons", self)
        self.delete_button.clicked.connect(self.delete_duplicates)
        self.layout.addWidget(self.delete_button)

        self.setLayout(self.layout)

    # Fonction pour ouvrir le dialogue de sélection de dossier
    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Sélectionner le dossier")
        if folder:
            self.path_text.setText(folder)

    # Fonction pour supprimer les doublons dans le dossier sélectionné
    def delete_duplicates(self):
        folder = self.path_text.text()
        if folder and os.path.isdir(folder):
            doublons = lister_doublons(folder)
            if doublons:
                supprimer_fichiers(doublons)
                QMessageBox.information(self, "Succès", "Les fichiers doublons ont été supprimés.")
            else:
                QMessageBox.information(self, "Info", "Aucun fichier doublon trouvé.")
        else:
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner un dossier valide.")