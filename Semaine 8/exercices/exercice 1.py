from PySide6.QtCore import QRectF, QSize, Qt, QPointF, QTimer
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import (QApplication, QGraphicsView, QGraphicsScene,
                               QVBoxLayout, QGraphicsPixmapItem, QFrame, QHBoxLayout, QPushButton, QGraphicsItem)

import random


class Bombardier(QFrame):

    VITESSE_AVION = 7
    POS_X_AVION = -100
    POS_Y_AVION = 0

    GRAVITE = 10
    FRICTION_AIR = 5

    def __init__(self):
        super().__init__()

        # mise en place de l'application

        self.setWindowTitle("Bombardier")
        self.setWindowIcon(QIcon("./../exemples/images/airplane.png"))

        self.setFixedSize(800, 600)

        self.layout_principal = QVBoxLayout()
        self.setLayout(self.layout_principal)

        # Création de l'environnement de l'animation

        self.vue_graphique = QGraphicsView()
        self.layout_principal.addWidget(self.vue_graphique)

        self.scene_graphique = QGraphicsScene(QRectF(0, 0, 500, 500))
        self.vue_graphique.setScene(self.scene_graphique)

        # Création avion

        self.avion_pixmap = QPixmap("./../exemples/images/airplane.png")
        self.avion_pixmap = self.avion_pixmap.scaled(QSize(64, 64), Qt.AspectRatioMode.KeepAspectRatio,
                                                     Qt.TransformationMode.SmoothTransformation)

        self.item_avion = QGraphicsPixmapItem(self.avion_pixmap)
        self.item_avion.setPos(QPointF(self.POS_X_AVION, self.POS_Y_AVION))

        self.scene_graphique.addItem(self.item_avion)

        # Bouton_Commencer / Stop
        self.layout_boutons = QHBoxLayout()
        self.layout_principal.addLayout(self.layout_boutons)

        self.bouton_commencer = QPushButton("Commencer")
        self.bouton_commencer.clicked.connect(self.commencer_animation)
        self.layout_boutons.addWidget(self.bouton_commencer)

        self.bouton_stop = QPushButton("Stop")
        self.bouton_stop.clicked.connect(self.stop)
        self.bouton_stop.setEnabled(False)
        self.layout_boutons.addWidget(self.bouton_stop)

        # Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.animation)
        self.timer.setInterval(50)

        # Création de la bombe
        self.bombe_creee = False
        self.item_bombe: None | QGraphicsItem = None

        # Création de la cible
        self.cible_pixmap = QPixmap("./../exemples/images/target.png")
        self.cible_pixmap = self.cible_pixmap.scaled(QSize(64, 64), Qt.AspectRatioMode.KeepAspectRatio,
                                                     Qt.TransformationMode.SmoothTransformation)

        self.item_cible = QGraphicsPixmapItem(self.cible_pixmap)
        self.item_cible.setPos(random.randint(0, 550), 450)

        self.scene_graphique.addItem(self.item_cible)

    def commencer_animation(self):
        self.bouton_commencer.setEnabled(False)
        self.bouton_stop.setEnabled(True)

        self.timer.start()

    def animation(self):
        self.item_avion.setPos(self.item_avion.pos().x() + self.VITESSE_AVION, self.POS_Y_AVION)

        if self.bombe_creee:
            self.item_bombe.setPos(self.item_bombe.pos().x() + self.FRICTION_AIR, self.item_bombe.pos().y() +
                                   self.GRAVITE)

    def stop(self):
        self.bouton_stop.setEnabled(False)
        self.bouton_commencer.setEnabled(True)

        self.timer.stop()

    def creer_bombe(self):
        bombe_pixmap = QPixmap("./../exemples/images/nuclear-bomb.png")
        bombe_pixmap = bombe_pixmap.scaled(QSize(32, 32), Qt.AspectRatioMode.KeepAspectRatio,
                                           Qt.TransformationMode.SmoothTransformation)

        self.item_bombe: QGraphicsPixmapItem = QGraphicsPixmapItem(bombe_pixmap)
        self.item_bombe.setPos(self.item_avion.pos())

        self.scene_graphique.addItem(self.item_bombe)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_B:
            if self.bombe_creee:
                super().keyPressEvent(event)
            else:
                self.creer_bombe()
                self.bombe_creee = True
        else:
            super().keyPressEvent(event)


app = QApplication()
bd = Bombardier()
bd.show()
app.exec()
