from toimintalogiikka.pelimuodot.pelimuoto import Pelimuoto
from toimintalogiikka.vastustaja.tekoaly import Tekoaly


class KPSTekoaly(Pelimuoto):
    def __init__(self):
        self._vastustaja = Tekoaly()

    def _pelaa(self):
        self._ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        self._tokan_siirto = self._vastustaja.anna_siirto()
        print(f"Tietokone valitsi: {self._tokan_siirto}")
