from toimintalogiikka.tuomari import Tuomari


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