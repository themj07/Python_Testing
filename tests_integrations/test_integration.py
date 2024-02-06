# test_integration.py
import unittest
import json
from app import loadClubs, loadCompetitions

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.clubs = loadClubs('clubs.json')
        self.competitions = loadCompetitions('competitions.json')

    def test_loadClubs(self):
        # Vérifiez que loadClubs renvoie une liste
        self.assertIsInstance(self.clubs, list)
        # Vérifiez que chaque élément de la liste est un dictionnaire (ou tout autre format attendu)
        for club in self.clubs:
            self.assertIsInstance(club, dict)

    def test_loadCompetitions(self):
        # Vérifiez que loadCompetitions renvoie une liste
        self.assertIsInstance(self.competitions, list)
        # Vérifiez que chaque élément de la liste est un dictionnaire (ou tout autre format attendu)
        for competition in self.competitions:
            self.assertIsInstance(competition, dict)

if __name__ == '__main__':
    unittest.main()
