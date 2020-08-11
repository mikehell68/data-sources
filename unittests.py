import unittest

class Random_UnitTests(unittest.TestCase):
    x = 1
    y = 2

    def test_add(self):
        self.assertTrue(self.y > self.x)
