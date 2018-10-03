import statistics as stats
import unittest

import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from config import  ROOT_DIR


class TestAverage(unittest.TestCase):
    def test_average(self):
        print(os.getcwd())
        file = open('dates.txt', 'r')
        data = file.readlines()
        dates = []
        for line in data:
            dates.append(int(line))
        avg = stats.mean(dates)
        disp = stats.stdev(dates)
        pLastLaunch = os.path.join(ROOT_DIR, 'tests/last_launch.txt')
        log_launch = open(pLastLaunch, 'r')
        avg_age = float(log_launch.readline())
        dispersion = float(log_launch.readline())
        log_launch.close()
        file.close()
        self.assertAlmostEqual(avg, avg_age, delta=3)
        self.assertAlmostEqual(disp, dispersion, delta=3)
