 
 
import os
import unittest
 
from app import app

class BasicTests(unittest.TestCase):
 
    # executed prior to each test
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_main_page(self):
        response = self.client.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_twitter_in_main_page(self):
        response = self.client.get('/', follow_redirects=True)
        self.assertIn(b"@Sim4n6", response.data)

    # executed after each test
    def tearDown(self):
        pass
 
 
if __name__ == "__main__":
    unittest.main()