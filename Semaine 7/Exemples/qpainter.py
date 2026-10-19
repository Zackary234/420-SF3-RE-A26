from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QPainter, QPixmap, QColorConstants
from PySide6.QtCore import QSize


class QPainterEx(QMainWindow):

    def __init__(self):
        super().__init__()

        self.etiquette_centrale = QLabel()
        # Création d'un canevas d'une largeur de 500 pixels et d'une hauteur de 400 pixels
        canevas = QPixmap(QSize(500, 400))
        # Remplir le canevas d'une couleur
        canevas.fill(QColorConstants.Cyan)

        self.etiquette_centrale.setPixmap(canevas)
        self.setCentralWidget(self.etiquette_centrale)

        self.dessiner()

    def dessiner(self):
        # Retrouver le pixmap pour notre canevas via notre QLabel
        canevas = self.etiquette_centrale.pixmap()
        # Initialise le painter
        painter = QPainter(canevas)
        # Dessiner une ligne de (25,50) à (150,150)
        painter.drawLine(25, 50, 150, 150)
        painter.drawText(150, 200, "Il est temps de dessiner!")
        # (x, y, largeur en pixel, hauteur en pixel), (x, y) étant le coin en haut à gauche
        painter.drawRect(65, 250, 90, 75)
        # SUPER IMPORTANT, appeler le .end() pour relâcher le QPainter
        painter.end()
        # On remet le canevas (QPixmap) sur le QLabel
        self.etiquette_centrale.setPixmap(canevas)


app = QApplication()
qp = QPainterEx()
qp.show()
app.exec()
