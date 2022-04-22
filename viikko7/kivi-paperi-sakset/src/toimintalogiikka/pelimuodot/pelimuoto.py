from toimintalogiikka.tuomari import Tuomari


class Pelimuoto:
    def __init__(self):
        self._tuomari = Tuomari()
        self._vastustaja = None
        self._tekoalyvastustaja = None

    def suorita(self):
        self.pelaa()
        while self._onko_ok_siirto(self._ekan_siirto) \
                and self._onko_ok_siirto(self._tokan_siirto):
            self._tuomari.kirjaa_siirto(self._ekan_siirto, self._tokan_siirto)
            print(self._tuomari)

            self.pelaa()

        print("Kiitos!")
        print(self._tuomari)

    def pelaa(self):
        self._ekan_siirto = None
        self._tokan_siirto = None

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"