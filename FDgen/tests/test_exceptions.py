import unittest
import sys
import config
import os
config.avg_age = 228
config.dispersion = 150

path = os.path.abspath('..')
path = os.path.dirname(path)
sys.path.append(path)
import FDgen

class ExpectedExceptionTestCase(unittest.TestCase):
    def test_max_avg(self):
        self.assertRaises(ValueError, FDgen.create_person)
