from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self._ostokset_list = []

    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 
        lukumaarat = map(lambda ostos: ostos.lukumaara(), self._ostokset_list)
        return sum(lukumaarat)

    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        hinnat = map(lambda ostos: ostos.hinta(), self._ostokset_list)
        return sum(hinnat)

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        for ostos in self._ostokset_list:
            if ostos.tuotteen_nimi() == lisattava.nimi():
                ostos.muuta_lukumaaraa(1)
                break
        else:
            self._ostokset_list.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        for i, ostos in enumerate(self._ostokset_list):
            if ostos.tuotteen_nimi() == poistettava.nimi():
                ostos.muuta_lukumaaraa(-1)
                if ostos.lukumaara() == 0:
                    del self._ostokset_list[i]
                break

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self._ostokset_list
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
