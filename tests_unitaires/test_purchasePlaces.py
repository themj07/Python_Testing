import unittest
from flask import flash
from app import app, competitions, clubs

class TestPurchasePlaces(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_purchasePlaces(self):
        # DONNÉES FICTIVES POUR LA REQUÊTE POST
        data = {
            'competition': 'Spring Festival',
            'club': 'Iron Temple',
            'places': '2'
        }

        # OBTENTION DU NOMBRE DE PLACES AVANT LA RÉSERVATION
        competition_before_booking = next((c for c in competitions if c['name'] == data['competition']), None)
        places_before_booking = int(competition_before_booking['numberOfPlaces'])

        # APPEL DE LA ROUTE PURCHASEPLACES AVEC LES DONNÉES FICTIVES DE TEST
        response = self.app.post('/purchasePlaces', data=data, follow_redirects=True)

        # CLUB ET COMPÉTITION APRÈS L'ACHAT
        club_after_booking = next((c for c in clubs if c['name'] == data['club']), None)
        competition_after_booking = next((c for c in competitions if c['name'] == data['competition']), None)

        # MISE À JOUR DU NOMBRE DE PLACES
        places_after_booking = int(competition_after_booking['numberOfPlaces'])
        self.assertEqual(places_after_booking, places_before_booking - int(data['places']))

        # VÉRIFIER SI UN MESSAGE FLASH EST PRÉSENT
        self.assertIn(b'Great - Booking complete!', response.data)

        # VÉRIFIER SI WELCOME RENVOIE LES BONNES DONNÉES
        self.assertEqual(response.status_code, 200)
        
if __name__ == '__main__':
    unittest.main()


import unittest
from unittest.mock import patch
from app import app, competitions, clubs

class TestPurchasePlaces(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.competition = {'name': 'Competition 1', 'numberOfPlaces': 20}
        self.club = {'name': 'Club 1', 'canBuyMorePlaces': True}
        competitions.append(self.competition)
        clubs.append(self.club)

    def test_purchase_places(self):
        # Test successful purchase
        response = self.client.post('/purchasePlaces', data={
            'competition': 'Competition 1',
            'club': 'Club 1',
            'places': 5
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Great - Booking complete!', response.get_data(as_text=True))
        self.assertEqual(self.competition['numberOfPlaces'], 15)
        self.assertEqual(self.club.get('purchasedPlaces', 0), 5)
        self.assertTrue(self.club['canBuyMorePlaces'])

        # Test invalid number of places
        response = self.client.post('/purchasePlaces', data={
            'competition': 'Competition 1',
            'club': 'Club 1',
            'places': -1
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Error - Invalid number of places requested!', response.get_data(as_text=True))
        self.assertEqual(self.competition['numberOfPlaces'], 15)
        self.assertEqual(self.club.get('purchasedPlaces', 0), 5)
        self.assertTrue(self.club['canBuyMorePlaces'])

        # Test attempting to purchase more places than available
        response = self.client.post('/purchasePlaces', data={
            'competition': 'Competition 1',
            'club': 'Club 1',
            'places': 16
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Error - Invalid number of places requested!', response.get_data(as_text=True))
        self.assertEqual(self.competition['numberOfPlaces'], 15)
        self.assertEqual(self.club.get('purchasedPlaces', 0), 5)
        self.assertTrue(self.club['canBuyMorePlaces'])

        # Test attempting to purchase more than 12 places in total
        response = self.client.post('/purchasePlaces', data={
            'competition': 'Competition 1',
            'club': 'Club 1',
            'places': 8
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Error - You have already purchased 12 places!', response.get_data(as_text=True))
        self.assertEqual(self.competition['numberOfPlaces'], 15)
        self.assertEqual(self.club.get('purchasedPlaces', 0), 5)
        # self.assertFalse(self.club['canBuyMorePlaces'])

    def tearDown(self):
        competitions.clear()
        clubs.clear()

if __name__ == '__main__':
    unittest.main()