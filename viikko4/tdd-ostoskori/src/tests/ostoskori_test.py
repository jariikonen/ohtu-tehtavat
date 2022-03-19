import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_hinta_tuotteen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        viili = Tuote("Viili", 2)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(viili)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_hinta_tuotteiden_hintojen_summa(self):
        maito = Tuote("Maito", 3)
        viili = Tuote("Viili", 2)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(viili)

        self.assertEqual(self.kori.hinta(), 3+2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)
