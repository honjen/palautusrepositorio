import unittest
from statistics_service import StatisticsService, SortBy
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

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_existing_player(self):
        # etsi olemassa oleva pelaaja
        player = self.stats.search("Lemieux")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Lemieux")

    def test_search_nonexistent_player(self):
        # etsi olematon pelaaja
        player = self.stats.search("No One")
        self.assertIsNone(player)

    def test_team_returns_correct_players(self):
        # team palauttaa oikeat pelaajat
        players = self.stats.team("EDM")
        self.assertEqual(len(players), 3)
        self.assertEqual(players[0].name, "Semenko")
        self.assertEqual(players[1].name, "Kurri")
        self.assertEqual(players[2].name, "Gretzky")

    def test_team_returns_empty_list_for_nonexistent_team(self):
        # olematon joukkue palauttaa tyhjän listan
        nonexistent_team = self.stats.team("Nobodies")
        self.assertEqual(len(nonexistent_team), 0)

    def test_top_sorts_by_points(self):
        # top järjestys: pisteet
        top_players = self.stats.top(3, SortBy.POINTS)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Lemieux")
        self.assertEqual(top_players[2].name, "Yzerman")

    def test_top_sorts_by_goals(self):
        # top järjestys: maalit
        top_players = self.stats.top(3, SortBy.GOALS)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Lemieux")
        self.assertEqual(top_players[1].name, "Yzerman")
        self.assertEqual(top_players[2].name, "Kurri")

    def test_top_sorts_by_assists(self):
        # top järjestys: syötöt
        top_players = self.stats.top(3, SortBy.ASSISTS)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Yzerman")
        self.assertEqual(top_players[2].name, "Lemieux")

    def test_top_defaults_to_points_if_no_sort_by_provided(self):
        # top ilman järjestystä
        top_players = self.stats.top(3)
        self.assertEqual(len(top_players), 3)
        self.assertEqual(top_players[0].name, "Gretzky")
        self.assertEqual(top_players[1].name, "Lemieux")
        self.assertEqual(top_players[2].name, "Yzerman")