import unittest
from main.crud import delete


class Testdelete(unittest.TestCase):
    def test_create(self):
        self.assertEqual(delete(), True)
