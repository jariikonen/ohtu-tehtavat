import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(PlayerReaderStub())

    def test_konstruktori_luo_olion_oikeilla_pelaajilla(self):
        self.assertEqual(len(self.statistics._players), 5)
        self.assertEqual(self.statistics._players[0].name, 'Semenko')
        self.assertEqual(self.statistics._players[4].name, 'Gretzky')

    def test_search_antaa_oikeat_tiedot(self):
        player = self.statistics.search('Kurri')
        self.assertEqual(str(player), 'Kurri EDM 37 + 53 = 90')

    def test_search_antaa_none_jos_pelaajaa_ei_loydy(self):
        player = self.statistics.search('Huberdeau')
        self.assertEqual(player, None)

    def test_team_antaa_oikeat_pelaajat(self):
        players = self.statistics.team('EDM')
        self.assertEqual(players[0].name, 'Semenko')
        self.assertEqual(players[1].name, 'Kurri')
        self.assertEqual(players[2].name, 'Gretzky')

    def test_top_scorers_antaa_oikean_listan(self):
        top_scorers = self.statistics.top_scorers(3)
        self.assertEqual(top_scorers[0].name, 'Gretzky')
        self.assertEqual(top_scorers[1].name, 'Lemieux')
        self.assertEqual(top_scorers[2].name, 'Yzerman')
