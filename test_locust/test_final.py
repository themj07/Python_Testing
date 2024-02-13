import unittest
from app import *
import os

from app import loadClubs

class TestBookingRoute(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_booking(self):
        response = self.app.get('/book/Fall%20Classic/Iron%20Temple')
        self.assertEqual(response.status_code, 200)
        

if __name__ == '__main__':
    unittest.main()

class TestLoadClubs(unittest.TestCase):
    def test_loadClubs(self):
        # Créez un fichier JSON de test avec des données fictives pour les clubs
        test_json_data = '{"clubs": ["Club A", "Club B", "Club C"]}' 
        with open('test_clubs.json', 'w') as test_file:
            test_file.write(test_json_data)
        # Appel de la fonction loadClubs pour charger les clubs à partir du fichier de test
        loaded_clubs = loadClubs('test_clubs.json')
        # Vérifiez si les clubs ont été chargés correctement
        self.assertEqual(loaded_clubs, ["Club A", "Club B", "Club C"])
        os.remove('test_clubs.json')

if __name__ == '__main__':
    unittest.main()

class TestloadCompetitions:
    def test_loadCompetitions(self):
        with open('test_competitions.json') as f:
            data = json.load(f)
        current_date = datetime.datetime.now()
        competitions = [competition for competition in data.get('competitions', []) if datetime.datetime.strptime(competition["date"], "%Y-%m-%d %H:%M:%S") >= current_date]
        chargComp = loadCompetitions('test_competitions.json')
        self.assertEqual(chargComp, competitions)

class TestloadClubs:
    def test_loadClubs(self):
        with open('test_clubs.json') as f:
            data = json.load(f)
        clubs = data.get('clubs', [])
        chargClubs = loadClubs('test_clubs.json')
        self.assertEqual(chargClubs, clubs)

if __name__ == "__main__":
    unittest.main()

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

class TestShowSummary(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_showSummary(self):
       
        data = {'email': 'admin@irontemple.com'} 
        response = self.app.post('/showSummary', data=data)
        self.assertEqual(response.status_code, 200)
        

if __name__ == '__main__':
    unittest.main()

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

    def tearDown(self):
        competitions.clear()
        clubs.clear()

if __name__ == '__main__':
    unittest.main()


class TestLogoutFunction(unittest.TestCase):
    
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_logout_redirect(self):
        # Effectuer une requête GET vers la route /logout
        response = self.app.get('/logout', follow_redirects=True)
        
        # Vérifier si la redirection vers la page d'accueil a eu lieu
        self.assertEqual(response.status_code, 200)  # Code de statut 200 indique succès
        # self.assertIn(b'index', response.data)  # Vérifie la présence du contenu de la page d'accueil

if __name__ == '__main__':
    unittest.main()


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

    def tearDown(self):
        competitions.clear()
        clubs.clear()

if __name__ == '__main__':
    unittest.main()
