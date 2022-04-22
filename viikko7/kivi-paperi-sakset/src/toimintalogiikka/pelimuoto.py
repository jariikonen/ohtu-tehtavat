from toimintalogiikka.tuomari import Tuomari
from toimintalogiikka.tekoaly import Tekoaly
from toimintalogiikka.tekoaly_parannettu import TekoalyParannettu


class Pelimuoto:
    def suorita(self):
        tuomari = Tuomari()
        self._pelaa()
        while self._onko_ok_siirto(self._ekan_siirto) \
                and self._onko_ok_siirto(self._tokan_siirto):
            tuomari.kirjaa_siirto(self._ekan_siirto, self._tokan_siirto)
            print(tuomari)

            self._pelaa()

        print("Kiitos!")
        print(tuomari)

    # template-metodi
    def _pelaa(self):
        self._ekan_siirto = None
        self._tokan_siirto = None

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"

    @staticmethod
    def luo_kaksinpeli():
        return KPSPelaajaVsPelaaja()

    @staticmethod
    def luo_yksinpeli():
        return KPSTekoaly()

    @staticmethod
    def luo_haastava_yksinpeli():
        return KPSParempiTekoaly()


class KPSPelaajaVsPelaaja(Pelimuoto):
    def _pelaa(self):
        self._ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        self._tokan_siirto = input("Toisen pelaajan siirto: ")


class KPSTekoaly(Pelimuoto):
    def __init__(self):
        self._vastustaja = Tekoaly()

    def _pelaa(self):
        self._ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        self._tokan_siirto = self._vastustaja.anna_siirto()
        print(f"Tietokone valitsi: {self._tokan_siirto}")


class KPSParempiTekoaly(Pelimuoto):
    def __init__(self):
        self._vastustaja = TekoalyParannettu(10)

    def _pelaa(self):
        self._ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        self._tokan_siirto = self._vastustaja.anna_siirto()
        self._vastustaja.aseta_siirto(self._ekan_siirto)
        print(f"Tietokone valitsi: {self._tokan_siirto}")
