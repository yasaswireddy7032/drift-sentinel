import unittest
from app import *

class DriftTests(unittest.TestCase):
    def test_identity(self):self.assertAlmostEqual(monitor(list(range(100)),list(range(100)))['psi'],0)
    def test_shift(self):self.assertEqual(monitor(list(range(100)),list(range(300,400)))['status'],'investigate')
    def test_missing(self):self.assertEqual(monitor([1,2,3],[None,None])['status'],'insufficient_data')
    def test_fixed_bins(self):self.assertEqual(monitor([1,2,3],[100])['bin_edges'],fit_bins([1,2,3]))
    def test_empty(self):
        with self.assertRaises(ValueError):monitor([1],[])

if __name__ == '__main__': unittest.main()
