import sys
from View.mainWindow import *
from fileManager import *
from PySide6.QtWidgets import QApplication


# Fonction principale
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    