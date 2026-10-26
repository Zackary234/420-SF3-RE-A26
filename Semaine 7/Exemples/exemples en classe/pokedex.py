import pandas as pd
from PySide6.QtWidgets import QApplication, QFrame, QVBoxLayout, QHBoxLayout, QLabel, QGridLayout, QComboBox


class PokeDex(QFrame):

    def __init__(self):
        super().__init__()

        self.disposition_principale = QVBoxLayout()
        self.setLayout(self.disposition_principale)

        self.disposition_info_pokedex = QGridLayout()
        self.disposition_principale.addLayout(self.disposition_info_pokedex)

        df: pd.DataFrame = self.import_data("./pokedex.csv")
        df.info()

        self.info_nb_label = QLabel(f"Nombre d'entrées: {df["pokedex_number"].count()}")
        self.disposition_info_pokedex.addWidget(self.info_nb_label, 1, 1)

        self.info_moyenne_attack = QLabel(f"Moyenne des attaques: {df["attack"].mean():.2f}")
        self.disposition_info_pokedex.addWidget(self.info_moyenne_attack, 1, 2)

        groupe_type1 = df.groupby("type_1")
        print(groupe_type1.count())
        print(df.groupby("type_2").count())

        self.liste_noms = QComboBox()
        df_triee = df.sort_values(by="name", ascending=True)
        liste_noms_series = df_triee["name"]
        self.liste_noms.addItems(liste_noms_series)

        self.disposition_principale.addWidget(self.liste_noms)

        series_basse_attaque = df[df["attack"] < 80]
        print(series_basse_attaque)









        hauteur: int | None = self.retourne_int_none(True)





    def import_data(self, nom_fichier_csv) -> pd.DataFrame:
        df = pd.read_csv(nom_fichier_csv)
        return df

    def retourne_int_none(self, is_none: bool):
        if is_none:
            return None
        return 42


app = QApplication()
poke = PokeDex()
poke.show()
app.exec()
