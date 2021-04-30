import unittest
import cal

class testCaseAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(cal.add(10,5), 15)
        #fail
    def test_add2(self):
        self.assertEqual(cal.add(2,1), 7)
    def test_add3(self):
        self.assertEqual(cal.add(8,2), 10)
        
    def test_sub(self):
        self.assertEqual(cal.sub(10,2), 8)
    def test_sub1(self):
        self.assertEqual(cal.sub(4,2), 2)
        #fail
    def test_sub2(self):
        self.assertEqual(cal.sub(7,2), 2 )

        #fail
    def test_mult(self):
        self.assertEqual(cal.mult(2,5), 1) 
    def test_mult2(self):
        self.assertEqual(cal.mult(10,2), 20)
    def test_mult3(self):
        self.assertEqual(cal.mult(2,5), 10)
    
        
    def test_div(self):
        self.assertEqual(cal.div(10,2), 5)
    def test_div(self):
        self.assertEqual(cal.div(8,2), 4)
        #fail
    def test_div(self):
        self.assertEqual(cal.div(10,2), 3)



if __name__ == '__main__':
    unittest.main()