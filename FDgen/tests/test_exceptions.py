import unittest
import sys
sys.path.append('..\..')
import config
config.avg_age = 228
config.dispersion = 150
import FDgen

class ExpectedExceptionTestCase(unittest.TestCase):
    def test_max_avg(self):
        self.assertRaises(ValueError, FDgen.create_person)
