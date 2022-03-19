import unittest
import main

class TestStringMethods(unittest.TestCase):

    def test_main_takes_file_and_iterations(self):
        app = main.Main("file", 1)
        self.assertEqual(app.FILE, "file")
        self.assertEqual(app.ITERATIONS, 1)
