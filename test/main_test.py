import unittest
import main

class TestStringMethods(unittest.TestCase):

    def test_main_takes_file_and_iterations(self):
        app = main.Main("glider.rle", 1)
        self.assertEqual(app.FILE, "glider.rle")
        self.assertEqual(app.ITERATIONS, 1)

    def test_file_parses_x_and_y(self):
        app = main.Main("./glider.rle", 1)
        self.assertEqual(app.get_width(), 3)
        self.assertEqual(app.get_height(), 3)