import unittest

from src.metricas import distancia_manhattan
from src.metricas import distancia_hamming
from src.metricas import distancia_euclideana
from src.metricas import norma_infinito

class MyTestCase(unittest.TestCase):
    def test_manhattan(self):
        self.assertEqual(distancia_manhattan([1, 2],[5,3]), 5)

    def test_hamming(self):
        self.assertEqual(distancia_hamming([1, 0, 6, 6],[5, 0, 6, 4]), 2)

    def test_euclideana(self):
        self.assertEqual(distancia_euclideana([3, 5],[0, 1]), 5)

    def test_norma_infinito(self):
        self.assertEqual(norma_infinito([1, 0, 2, 4],[1, 2, 1, 1]), 3)

if __name__ == '__main__':
    unittest.main()
