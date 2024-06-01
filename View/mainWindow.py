import os
from fileManager import lister_doublons
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QFileDialog, QMessageBox, QCheckBox
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from View.duplicateFilesDialog import DuplicateFilesDialog

# Classe principale de la fenêtre
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TANOS")

        # Définir l'icône de la fenêtre
        self.setWindowIcon(QIcon("assets/icon.png"))

        # Définir la taille fixe de la fenêtre
        self.setFixedSize(400, 200)

        # Désactiver les boutons de maximisation et de redimensionnement
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint & ~Qt.WindowMinimizeButtonHint)
        self.setWindowFlags(self.windowFlags() | Qt.WindowCloseButtonHint)
        
        self.layout = QVBoxLayout()

        # Zone de texte pour afficher le chemin du dossier sélectionné
        self.path_text = QLineEdit(self)
        self.layout.addWidget(self.path_text)

        # Checkbox pour la recherche récursive
        self.recursive_checkbox = QCheckBox("Récursif", self)
        self.layout.addWidget(self.recursive_checkbox)

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
        recursive = self.recursive_checkbox.isChecked()
        if folder and os.path.isdir(folder):
            doublons = lister_doublons(folder, recursive)
            if doublons:
                self.duplicate_files_window = DuplicateFilesDialog(doublons, self)
                self.duplicate_files_window.exec_()
            else:
                QMessageBox.information(self, "Info", "Aucun fichier doublon trouvé.")
        else:
            QMessageBox.warning(self, "Erreur", "Veuillez sélectionner un dossier valide.")
