import unittest
import scipy.stats
from main import *

class UnitTests(unittest.TestCase) :
    def test_f_generation(self) :
        for i in range(2,5) :
            for j in range(2,5) :
                t = gen_f_variable( i, j )
                pval = scipy.stats.f.cdf( t, i-1, j-1 )
                self.assertTrue( pval>0.005 and pval<0.995, "your gen_f_variable does not appear to be sampling from the correct distribution" )
