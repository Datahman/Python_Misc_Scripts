import unittest 
import math
import factorial
from test import test_support

class FactorialTest(unittest.TestCase):
    def setUp(self):
        print ("setup")
        
    def tearDown(self):
        print ("cleanup")
        
    def test_positives(self):
        for x in range(1,10+1):
            actual = math.factorial(x)
            val=factorial.fact(x)
            print ("%d! = %g == %g"%(x,val,actual))
            self.assertAlmostEqual(actual, val, 1e-1) # check 
            
        def test_negative(self):
            passed = False
            try:
                factorial.fact(-3)
            except Exception as e:
                passed = True and (e.message.find("Cannot calculate ")>=0)
            self.assertTrue(passed)
            
if __name__=="__main__":
    test_support.run_unittest(FactorialTest)