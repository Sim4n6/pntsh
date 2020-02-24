 
 
import os
import unittest
 
from app import app

class DebugTests(unittest.TestCase):
 
    # executed prior to each test
    def setUp(self):
        pass

    def test_debug_mode(self):
        self.assertFalse(app.config["DEBUG"])

    # executed after each test
    def tearDown(self):
        pass
 
 
if __name__ == "__main__":
    unittest.main()