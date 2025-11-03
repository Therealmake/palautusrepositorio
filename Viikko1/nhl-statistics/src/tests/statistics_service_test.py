import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_creating_contructor(self):
        self.assertIsInstance(self.stats, StatisticsService)
        self.assertIsInstance(self.stats._players, list)

    def test_search(self):
        self.assertEqual(self.stats.search("Semenko").name, "Semenko")
        self.assertEqual(type(self.stats.search("Semenko")), Player)
        self.assertEqual(len(self.stats._players), 5)
        self.assertTrue(self.stats.search("Gretzky"))
        self.assertIsNone(self.stats.search("Ville Vallaton"))

    def test_team(self):
        self.assertEqual(len(self.stats.team("EDM")), 3)
        self.assertEqual(len(self.stats.team("PIT")), 1)
        self.assertEqual(len(self.stats.team("DET")), 1)
        self.assertEqual(len(self.stats.team("CHI")), 0)
        self.assertEqual(self.stats.team("EDM")[2].name, "Gretzky")

    def test_top_points(self):
        top = self.stats.top(3, SortBy.POINTS)
        self.assertEqual([p.name for p in top], ["Gretzky", "Lemieux", "Yzerman"])

    def test_top_goals(self):
        top = self.stats.top(3, SortBy.GOALS)
        self.assertEqual([p.name for p in top], ["Lemieux", "Yzerman", "Kurri"])

    def test_top_assists(self):
        top = self.stats.top(3, SortBy.ASSISTS)
        self.assertEqual([p.name for p in top], ["Gretzky", "Yzerman", "Lemieux"])