from toimintalogiikka.pelimuodot.pelimuoto import Pelimuoto


class KPSPelaajaVsPelaaja(Pelimuoto):
    def __init__(self):
        super().__init__()

    def pelaa(self):
        self._ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        self._tokan_siirto = input("Toisen pelaajan siirto: ")
