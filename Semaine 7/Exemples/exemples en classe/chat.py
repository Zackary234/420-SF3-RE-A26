from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QPainter, QPen, QPixmap, QBrush, QColor, QColorConstants, QTransform, QPainterPath
from PySide6.QtCore import QSize, QRect, QPoint, Qt


class Chat(QLabel):

    def __init__(self):
        super().__init__()

        self.canevas = QPixmap(QSize(800, 800))
        pixmap_tuile = QPixmap("./image/gazon.png")
        painter = QPainter(self.canevas)
        painter.drawTiledPixmap(QRect(0, 0, 800, 800), pixmap_tuile)

        couleur = QColor(245, 167, 66)

        pinceau_remplissage = QBrush()
        pinceau_remplissage.setStyle(Qt.BrushStyle.SolidPattern)
        pinceau_remplissage.setColor(couleur)

        pen = QPen()
        pen.setColor(couleur)
        painter.setPen(pen)
        painter.setBrush(pinceau_remplissage)

        # corps
        painter.drawEllipse(QPoint(400, 400), 200, 100)

        # tête
        painter.drawEllipse(QPoint(200, 300), 80, 80)

        # pattes
        painter.drawRect(225, 450, 25, 75)
        painter.drawRect(325, 475, 25, 75)
        painter.drawRect(425, 475, 25, 75)
        painter.drawRect(525, 455, 25, 75)

        # yeux
        brosse_yeux = QBrush()
        brosse_yeux.setStyle(Qt.BrushStyle.SolidPattern)
        brosse_yeux.setColor(QColorConstants.Black)
        crayon_yeux = QPen()
        crayon_yeux.setWidth(15)
        crayon_yeux.setBrush(brosse_yeux)

        painter.setPen(crayon_yeux)
        painter.drawPoint(QPoint(160, 260))
        painter.drawPoint(QPoint(240, 260))

        # Nez
        crayon_nez = QPen()
        crayon_nez.setColor(QColorConstants.Red)
        crayon_nez.setWidth(10)
        painter.setPen(crayon_nez)
        painter.drawPoint(QPoint(200, 300))

        # moustache
        crayon_moustache = QPen()
        crayon_moustache.setWidth(3)
        painter.setPen(crayon_moustache)
        transform_moustache = QTransform()
        transform_moustache.translate(200, 300)

        painter.setTransform(transform_moustache)
        painter.drawLine(0, 0, 40, 0)

        transform_moustache.rotate(-30)
        painter.setTransform(transform_moustache)
        painter.drawLine(0, 0, 40, 0)

        transform_moustache.rotate(60)
        painter.setTransform(transform_moustache)
        painter.drawLine(0, 0, 40, 0)

        transform_moustache.rotate(120)
        painter.setTransform(transform_moustache)
        painter.drawLine(0, 0, 40, 0)

        transform_moustache.rotate(30)
        painter.setTransform(transform_moustache)
        painter.drawLine(0, 0, 40, 0)

        transform_moustache.rotate(30)
        painter.setTransform(transform_moustache)
        painter.drawLine(0, 0, 40, 0)

        # Oreilles
        chemin_oreille = QPainterPath()
        chemin_oreille.lineTo(5, -50)
        chemin_oreille.lineTo(50, 0)
        chemin_oreille.closeSubpath()

        transform_oreille = QTransform()
        transform_oreille.translate(140, 250)
        painter.setTransform(transform_oreille)

        crayon_oreilles = QPen()
        crayon_oreilles.setBrush(pinceau_remplissage)
        crayon_oreilles.setColor(couleur)
        painter.setPen(crayon_oreilles)
        painter.drawPath(chemin_oreille)

        transform_oreille.translate(75, 0)
        painter.setTransform(transform_oreille)
        painter.drawPath(chemin_oreille)



        painter.end()
        self.setPixmap(self.canevas)


app = QApplication()
chat = Chat()
chat.show()
app.exec()
