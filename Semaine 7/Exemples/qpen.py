from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QPainter, QPixmap, QColorConstants, QPen, QBrush, QColor, QPainterPath
from PySide6.QtCore import QSize, Qt


class QPainterEx(QMainWindow):

    def __init__(self):
        super().__init__()

        self.etiquette_centrale = QLabel()
        # Création d'un canevas d'une largeur de 800 pixels et d'une hauteur de 600 pixels
        canevas = QPixmap(QSize(800, 600))
        # Remplir le canevas d'une couleur
        # QColorConstants contient un ensemble de couleurs prédéfinies
        canevas.fill(QColorConstants.White)

        self.etiquette_centrale.setPixmap(canevas)
        self.setCentralWidget(self.etiquette_centrale)

        self.dessiner()

    def dessiner(self):
        # Retrouver le pixmap pour notre canevas via notre QLabel
        canevas = self.etiquette_centrale.pixmap()
        painter = QPainter(canevas)
        crayon = QPen()
        crayon.setWidth(30)
        pinceau = QBrush()
        # on change le style de brosse
        pinceau.setStyle(Qt.BrushStyle.Dense5Pattern)
        pinceau.setColor(QColorConstants.Red)
        crayon.setBrush(pinceau)
        painter.setPen(crayon)
        painter.drawLine(50, 50, 75, 100)
        crayon2 = QPen()
        # Une autre façon d'initialiser une couleur, en utilisant QColor(r, g, b)
        crayon2.setColor(QColor(24, 37, 112))
        crayon2.setWidth(15)
        # Les constantes pour PenCapStyle sont dans une class interne de Qt
        crayon2.setCapStyle(Qt.PenCapStyle.RoundCap)
        # de façon similaire pour les PenJointStyle
        crayon2.setJoinStyle(Qt.PenJoinStyle.RoundJoin)
        painter.setPen(crayon2)
        painter.drawPoint(200, 250)

        # On va faire un "chemin" à dessiner, une succession de formes
        chemin = QPainterPath()
        # commencer un sous-chemin
        chemin.moveTo(50, 50)
        chemin.lineTo(150, 50)
        # courbe de Bézier cubique
        chemin.cubicTo(200, 50, 200, 150, 150, 150)
        chemin.lineTo(50, 150)
        # ferme le sous-chemin, cela va compléter jusqu'au départ
        chemin.closeSubpath()

        # ajouter des formes simples
        chemin.addEllipse(250, 40, 120, 120)
        chemin.addRect(400, 40, 120, 120)

        # ajouter un arc (x, y, w, h, startAngle, sweepLength) en degrés
        chemin.moveTo(100, 250)

        # on dessine le chemin
        painter.drawPath(chemin)

        painter.end()
        self.etiquette_centrale.setPixmap(canevas)


app = QApplication()
qp = QPainterEx()
qp.show()
app.exec()
