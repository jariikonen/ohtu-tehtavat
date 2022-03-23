from enum import Enum
from tkinter import ttk, constants, StringVar


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4


class Kayttoliittyma:
    def __init__(self, sovelluslogiikka, root):
        self._sovelluslogiikka = sovelluslogiikka
        self._root = root

        self._komennot = {
            Komento.SUMMA: Summa(sovelluslogiikka, self._lue_syote),
            Komento.EROTUS: Erotus(sovelluslogiikka, self._lue_syote),
            Komento.NOLLAUS: Nollaus(sovelluslogiikka, self._lue_syote),
            Komento.KUMOA: Kumoa(sovelluslogiikka, self._lue_syote)
        }

    def kaynnista(self):
        self._tulos_var = StringVar()
        self._tulos_var.set(self._sovelluslogiikka.tulos)
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._tulos_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _lue_syote(self):
        return self._syote_kentta.get()

    def _suorita_komento(self, komento):
        komento_olio = self._komennot[komento]
        komento_olio.suorita()
        if self._sovelluslogiikka.edellinen_komento_olio:
            self._kumoa_painike["state"] = constants.NORMAL
        else:
            self._kumoa_painike["state"] = constants.DISABLED

        if self._sovelluslogiikka.tulos == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._tulos_var.set(self._sovelluslogiikka.tulos)


class KomentoLuokka:
    def __init__(self, sovelluslogiikka, lue_arvo):
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_arvo = lue_arvo

    def _lue_syote(self):
        arvo = 0

        try:
            arvo = int(self._lue_arvo())
        except Exception:
            pass

        return arvo

    def _talleta_edellinen_tulos(self):
        self._edellinen_tulos = self._sovelluslogiikka.tulos

    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._edellinen_tulos)


class Summa(KomentoLuokka):
    def __init__(self, sovelluslogiikka, lue_arvo):
        super().__init__(sovelluslogiikka, lue_arvo)

    def suorita(self):
        self._talleta_edellinen_tulos()
        self._sovelluslogiikka.plus(self._lue_syote())
        self._sovelluslogiikka.aseta_edellinen_komento(self)
        

class Erotus(KomentoLuokka):
    def __init__(self, sovelluslogiikka, lue_arvo):
        super().__init__(sovelluslogiikka, lue_arvo)

    def suorita(self):
        self._talleta_edellinen_tulos()
        self._sovelluslogiikka.miinus(self._lue_syote())
        self._sovelluslogiikka.aseta_edellinen_komento(self)


class Nollaus(KomentoLuokka):
    def __init__(self, sovelluslogiikka, lue_arvo):
        super().__init__(sovelluslogiikka, lue_arvo)

    def suorita(self):
        self._talleta_edellinen_tulos()
        self._sovelluslogiikka.nollaa()
        self._sovelluslogiikka.aseta_edellinen_komento(self)


class Kumoa(KomentoLuokka):
    def __init__(self, sovelluslogiikka, lue_arvo):
        super().__init__(sovelluslogiikka, lue_arvo)

    def suorita(self):
        if self._sovelluslogiikka.edellinen_komento_olio:
            self._sovelluslogiikka.edellinen_komento_olio.kumoa()
            self._sovelluslogiikka.aseta_edellinen_komento(None)