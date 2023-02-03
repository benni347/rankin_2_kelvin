import unittest
import main


class MyTestCase(unittest.TestCase):
    def test_rankine_to_kelvin(self):
        self.assertEqual(main.rankine_too_kelvin(491.67), "273.15 K")
        self.assertEqual(main.rankine_too_kelvin(459.67), "255.37 K")
        self.assertEqual(main.rankine_too_kelvin(500), "277.78 K")
        self.assertEqual(main.rankine_too_kelvin(100), "55.56 K")
        self.assertEqual(main.rankine_too_kelvin(0), "0.0 K")
        self.assertEqual(main.rankine_too_kelvin(20000), "11111.11 K")
        self.assertEqual(main.rankine_too_kelvin(-459.67), "-273.15 K")

if __name__ == '__main__':
    unittest.main()
