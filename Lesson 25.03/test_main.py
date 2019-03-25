from main import Calculus
import unittest

#pip install unittest --user
class TestCalculus(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculus(0,0).add(), 0)
        self.assertEqual(Calculus(1,2).add(), 3)
    def test_sub(self):
        self.assertEqual(Calculus(1,0).sub(), 1)
        self.assertEqual(Calculus(1,2).sub(), -1)

    def test_mult(self):
        self.assertEqual(Calculus(1,0).mult(), 0)
        self.assertEqual(Calculus(1,-2).mult(), -2)

    def test_div(self):
        self.assertEqual(Calculus(1,0).div(), 1)


        #self.assertTrue(Calculus(0,1).add())


if __name__ == '__main__':
    unittest.main()


