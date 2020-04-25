
import unittest
from main import add


class TestFunction(unittest.TestCase):
    def test_add(self):
        self.assertEquals(add(2, 2), 4)


unittest.main(argv=[''], verbosity=2, exit=False)
