from toimintalogiikka.pelimuodot.pelimuoto import Pelimuoto
from toimintalogiikka.tuomari import Tuomari
from toimintalogiikka.vastustaja.tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly(Pelimuoto):
    def __init__(self):
        self._vastustaja = TekoalyParannettu(10)

    def _pelaa(self):
        self._ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        self._tokan_siirto = self._vastustaja.anna_siirto()
        self._vastustaja.aseta_siirto(self._ekan_siirto)
        print(f"Tietokone valitsi: {self._tokan_siirto}")
