from toimintalogiikka.pelimuodot.pelimuoto import Pelimuoto


class KPSPelaajaVsPelaaja(Pelimuoto):
    def _pelaa(self):
        self._ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        self._tokan_siirto = input("Toisen pelaajan siirto: ")
