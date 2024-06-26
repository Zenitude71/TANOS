from PySide6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QCheckBox, QMessageBox, QScrollArea, QWidget

class DuplicateFilesDialog(QDialog):
    def __init__(self, doublons, to_trash, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Liste des doublons")
        self.setMinimumSize(400, 300)
        
        self.layout = QVBoxLayout()

        # Créer un QScrollArea pour contenir les fichiers doublons
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        
        # Créer un widget pour contenir les checkboxes
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)
        scroll_layout.setSpacing(0)  # Pas d'espace entre les éléments
        scroll_layout.setContentsMargins(0, 0, 0, 0)  # Pas de marges

        self.checkboxes = []

        # Ajouter une checkbox pour chaque fichier doublon
        for fichier in doublons:
            checkbox = QCheckBox(fichier, self)
            checkbox.setChecked(True)
            self.checkboxes.append(checkbox)
            scroll_layout.addWidget(checkbox)

        # Assurer que le contenu commence en haut du contenant
        scroll_layout.addStretch()

        scroll_area.setWidget(scroll_widget)
        self.layout.addWidget(scroll_area)

        # Bouton pour supprimer les fichiers sélectionnés
        self.delete_button = QPushButton("Supprimer", self)
        self.delete_button.clicked.connect(self.delete_selected_files)
        self.layout.addWidget(self.delete_button)

        self.setLayout(self.layout)

        self.doublons = doublons
        self.to_trash = to_trash

    def delete_selected_files(self):
        fichiers_a_supprimer = [checkbox.text() for checkbox in self.checkboxes if checkbox.isChecked()]

        if fichiers_a_supprimer:
            try:
                from fileManager import supprimer_fichiers, envoyer_a_la_corbeille
                if self.to_trash:
                    envoyer_a_la_corbeille(fichiers_a_supprimer)
                else:
                    supprimer_fichiers(fichiers_a_supprimer)
                QMessageBox.information(self, "Succès", f"{len(fichiers_a_supprimer)} fichiers doublons ont été traités.")
                self.accept()  # Fermer la fenêtre après traitement
            except Exception as e:
                QMessageBox.critical(self, "Erreur", f"Une erreur s'est produite lors du traitement des fichiers: {e}")
        else:
            QMessageBox.warning(self, "Info", "Aucun fichier sélectionné pour suppression.")
