# import os
# import json
# import unittest
# from app import loadClubs, loadCompetitions, showSummary
# from app import app

# class TestAppRoutes(unittest.TestCase):

#     def setUp(self):
#         self.app = app.test_client()

#     def test_book_valid_input(self):
#         with app.test_request_context('/book/PremierLeague/Arsenal'):
#             response = self.app.get('/book/PremierLeague/Arsenal')
#             self.assertEqual(response.status_code, 200)

#     def test_book_invalid_input(self):
#         with app.test_request_context('/book/InvalidCompetition/InvalidClub'):
#             response = self.app.get('/book/InvalidCompetition/InvalidClub')
#             self.assertEqual(response.status_code, 404)

# if __name__ == '__main__':
#     unittest.main()