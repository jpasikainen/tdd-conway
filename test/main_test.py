import unittest
import main

class TestFileParsingGlider(unittest.TestCase):
    app = None
    def setUp(self):
        self.app = main.Main("glider.rle", 0)

    def test_main_takes_file_and_iterations(self):
        self.assertEqual(self.app.FILE, "glider.rle")
        self.assertEqual(self.app.ITERATIONS, 0)

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
        self.app = main.Main("blinker.rle", 0)

    def test_main_takes_file_and_iterations(self):
        self.assertEqual(self.app.FILE, "blinker.rle")
        self.assertEqual(self.app.ITERATIONS, 0)

    def test_file_parses_x_and_y(self):
        self.assertEqual(self.app.get_width(), 3)
        self.assertEqual(self.app.get_height(), 1)
    
    def test_file_pattern_parsed(self):
        self.assertEqual(self.app.get_pattern(), ["ooo"])

class TestFileParsingGosper(unittest.TestCase):
    app = None
    def setUp(self):
        self.app = main.Main("gosperglidergun.rle", 0)

    def test_main_takes_file_and_iterations(self):
        self.assertEqual(self.app.FILE, "gosperglidergun.rle")
        self.assertEqual(self.app.ITERATIONS, 0)

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

class TestSimulationRules(unittest.TestCase):
    def test_neighbors_are_counted_correctly(self):
        # horizontal
        count = main.Main("glider.rle", 0).get_neighbors(0, 0)
        self.assertEqual(count, 1)
        # diagonal
        count = main.Main("glider.rle", 0).get_neighbors(1, 0)
        self.assertEqual(count, 1)
        # hor + diag
        count = main.Main("glider.rle", 0).get_neighbors(1, 2)
        self.assertEqual(count, 3)
    
    def test_less_than_two_neighbors_dies(self):
        app = main.Main("glider.rle", 1)
        self.assertEqual(app.get_cell(1, 0), "b")
    
    def test_less_than_two_neighbors_dies(self):
        app = main.Main("glider.rle", 1)
        self.assertEqual(app.get_cell(1, 2), "o")

    def test_more_than_three_neighbors_dies(self):
        app = main.Main("gosperglidergun.rle", 1)
        #self.assertEqual(app.get_cell(21, 3), "o")
        self.assertEqual(app.get_cell(21, 3), "b")
    
    def test_dead_with_three_neighbors_becomes_alive(self):
        app = main.Main("blinker.rle", 1)
        self.assertEqual(app.get_cell(1, 0), "o")

class TestSimulation(unittest.TestCase):
    def test_blinker_simulated_1_iter(self):
        app = main.Main("blinker.rle", 1)
        self.assertEqual(app.get_pattern(), ["bob", "bob", "bob"])
    
    def test_blinker_simulated_2_iter(self):
        app = main.Main("blinker.rle", 2)
        self.assertEqual(app.get_pattern(), ["bbb", "ooo", "bbb"])
    
    def test_blinker_simulated_2_iter(self):
        app = main.Main("blinker.rle", 10)
        self.assertEqual(app.get_pattern(), ["bbb", "ooo", "bbb"])