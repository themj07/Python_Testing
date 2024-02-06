import os
import json
import unittest
from app import loadClubs, loadCompetitions, showSummary
from app import app

def test_show_summary_with_valid_email(self):
    with self.app as client:
        response = client.post('/showSummary', data={'email': 'example@email.com'})
        self.assertEqual(response.status_code, 200)
        # Ajoutez d'autres assertions pour vérifier le contenu du template rendu

def test_show_summary_with_invalid_email(self):
    with self.app as client:
        response = client.post('/showSummary', data={'email': 'invalid@email.com'})
        self.assertEqual(response.status_code, 404)