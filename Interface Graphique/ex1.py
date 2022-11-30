import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)
        self.lab = QLabel("Saisir votre nom")
        self.text = QLineEdit("")
        self.labprenom = QLabel("")
        ok = QPushButton("Ok")
        quit = QPushButton("Quitter")

        # Ajouter les composants au grid layout
        grid.addWidget(self.lab, 0, 0)
        grid.addWidget(self.text, 1, 0)
        grid.addWidget(self.labprenom, 2, 0)
        grid.addWidget(ok, 3, 0)
        grid.addWidget(quit, 4, 0)

        # Actions
        ok.clicked.connect(self.__actionOk)
        quit.clicked.connect(self.__actionQuitter)

        self.setWindowTitle("Une première fenêtre")

    def __actionOk(self):
        prenom = self.text.text()
        self.labprenom.setText(f"Bonjour {prenom}")
    def __actionQuitter(self):
        QCoreApplication.exit(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()