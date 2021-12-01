import unittest

from adventofcode.measurement import (count_increases,
                                      count_increases_by_window)


class TestMeasurement(unittest.TestCase):
    def setUp(self):
        self.data = [199,
                     200,
                     208,
                     210,
                     200,
                     207,
                     240,
                     269,
                     260,
                     263]

    def test_count_increases(self):
        self.assertEqual(7, count_increases(self.data))

    def test_count_increases_by_window(self):
        self.assertEqual(5, count_increases_by_window(self.data, 3))
