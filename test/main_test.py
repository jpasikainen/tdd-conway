import unittest
import main

class TestFileParsing(unittest.TestCase):

    app = None
    def setUp(self):
        self.app = main.Main("glider.rle", 1)

    def test_main_takes_file_and_iterations(self):
        self.assertEqual(self.app.FILE, "glider.rle")
        self.assertEqual(self.app.ITERATIONS, 1)

    def test_file_parses_x_and_y(self):
        self.assertEqual(self.app.get_width(), 3)
        self.assertEqual(self.app.get_height(), 3)
    
    def test_file_pattern_parsed(self):
        self.assertEqual(self.app.get_pattern(), [["b", "o", "b"], ["b", "b", "o"], ["o", "o", "o"]])

