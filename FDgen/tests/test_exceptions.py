import unittest

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
import config
config.avg_age = 228
config.dispersion = 150

path = os.path.abspath('..')
path = os.path.dirname(path)
sys.path.append(path)
import FDgen

class ExpectedExceptionTestCase(unittest.TestCase):
    def test_max_avg(self):
        self.assertRaises(ValueError, FDgen.create_person)
