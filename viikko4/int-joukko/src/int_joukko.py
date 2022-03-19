KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Kapasiteetin täytyy olla positiivinen kokonaisluku")
        else:
            self.kapasiteetti = kapasiteetti

        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Kasvatuskoon täytyy olla positiivinen kokonaisluku")
        else:
            self.kasvatuskoko = kasvatuskoko

        self.joukko = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        if n in self.joukko:
            return True
        return False

    def lisaa(self, n):
        if len(self.joukko) == 0:
            self.joukko[0] = n
            return True

        if self.kuuluu(n):
            return False
        
        self.joukko[self.alkioiden_lkm] = n
        self.alkioiden_lkm += 1

        if self.alkioiden_lkm % len(self.joukko) == 0:
            self._kasvata_taulukkoa()

        return True

    def poista(self, n):
        for i in range(0, self.alkioiden_lkm):
            if n == self.joukko[i]:
                self.joukko[i] = 0
                self._tiivista(i)
                return True

        return False

    def _kasvata_taulukkoa(self):
        taulukko_old = self.joukko
        self._kopioi_taulukko(self.joukko, taulukko_old)
        self.joukko = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
        self._kopioi_taulukko(taulukko_old, self.joukko)

    def _kopioi_taulukko(self, a, b, pituus=None):
        if not pituus:
            pituus = len(a)

        for i in range(0, pituus):
            b[i] = a[i]

    def _tiivista(self, alkaen):
        for i in range(alkaen, self.alkioiden_lkm - 1):
            self.joukko[i] = self.joukko[i + 1]
        self.joukko[self.alkioiden_lkm] = 0
        self.alkioiden_lkm = self.alkioiden_lkm - 1

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm
        self._kopioi_taulukko(self.joukko, taulu, self.alkioiden_lkm)
        return taulu

    @staticmethod
    def yhdiste(a, b):
        yhdiste = IntJoukko()
        a_list = a.to_int_list()
        b_list = b.to_int_list()

        for i in range(0, len(a_list)):
            yhdiste.lisaa(a_list[i])

        for i in range(0, len(b_list)):
            yhdiste.lisaa(b_list[i])

        return yhdiste

    @staticmethod
    def leikkaus(a, b):
        leikkaus = IntJoukko()
        a_list = a.to_int_list()
        b_list = b.to_int_list()

        for i in range(0, len(a_list)):
            for j in range(0, len(b_list)):
                if a_list[i] == b_list[j]:
                    leikkaus.lisaa(b_list[j])

        return leikkaus

    @staticmethod
    def erotus(a, b):
        erotus = IntJoukko()
        a_list = a.to_int_list()
        b_list = b.to_int_list()

        for i in range(0, len(a_list)):
            erotus.lisaa(a_list[i])

        for i in range(0, len(b_list)):
            erotus.poista(b_list[i])

        return erotus

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.joukko[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.joukko[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.joukko[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
