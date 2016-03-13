import unittest

from src.metricas import distancia_manhattan
from src.metricas import distancia_hamming

class MyTestCase(unittest.TestCase):
    def test_manhattan(self):
        self.assertEqual(distancia_manhattan([1, 2],[5,3]), 5)

    def test_hamming(self):
        self.assertEqual(distancia_hamming([1, 0, 6, 6],[5, 0, 6, 4]), 0)

if __name__ == '__main__':
    unittest.main()
