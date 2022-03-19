import unittest
import main

class TestFileParsingGlider(unittest.TestCase):
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
        self.assertEqual(self.app.get_pattern(), ["bob", "bbo", "ooo"])

# .O.
# ..O
# OOO

class TestFileParsingBlinker(unittest.TestCase):
    app = None
    def setUp(self):
        self.app = main.Main("blinker.rle", 1)

    def test_main_takes_file_and_iterations(self):
        self.assertEqual(self.app.FILE, "blinker.rle")
        self.assertEqual(self.app.ITERATIONS, 1)

    def test_file_parses_x_and_y(self):
        self.assertEqual(self.app.get_width(), 3)
        self.assertEqual(self.app.get_height(), 1)
    
    def test_file_pattern_parsed(self):
        self.assertEqual(self.app.get_pattern(), ["ooo"])

class TestFileParsingGosper(unittest.TestCase):
    app = None
    def setUp(self):
        self.app = main.Main("gosperglidergun.rle", 1)

    def test_main_takes_file_and_iterations(self):
        self.assertEqual(self.app.FILE, "gosperglidergun.rle")
        self.assertEqual(self.app.ITERATIONS, 1)

    def test_file_parses_x_and_y(self):
        self.assertEqual(self.app.get_width(), 36)
        self.assertEqual(self.app.get_height(), 9)
    
    def test_file_pattern_parsed(self):
        self.assertEqual(self.app.get_pattern(), [
            "bbbbbbbbbbbbbbbbbbbbbbbbobbbbbbbbbbb",
            "bbbbbbbbbbbbbbbbbbbbbbobobbbbbbbbbbb",
            "bbbbbbbbbbbboobbbbbboobbbbbbbbbbbboo",
            "bbbbbbbbbbbobbbobbbboobbbbbbbbbbbboo",
            "oobbbbbbbbobbbbbobbboobbbbbbbbbbbbbb",
            "oobbbbbbbbobbboboobbbbobobbbbbbbbbbb",
            "bbbbbbbbbbobbbbbobbbbbbbobbbbbbbbbbb",
            "bbbbbbbbbbbobbbobbbbbbbbbbbbbbbbbbbb",
            "bbbbbbbbbbbboobbbbbbbbbbbbbbbbbbbbbb"
        ])

class TestSimulation(unittest.TestCase):
    def test_neighbors_are_counted_correctly(self):
        count = main.Main("glider.rle", 1).get_neighbors(0, 0)
        self.assertEqual(count, 1)