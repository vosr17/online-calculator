import main
import unittest

class MyTestCase(unittest.TestCase):

        def setUp(self):
            main.app.testing = True
            self.app = main.app.test_client()

        def test_divint(self):
            rv =  self.app.get('/division?A=7&B=6')
            self.assertEqual(b'1.16666666666667', rv.data)
        def test_divfloat(self):
            rv =  self.app.get('/division?A=7.5&B=2.5')
            self.assertEqual(b'3 \n', rv.data)
        def test_divfrac(self):
            rv =  self.app.get('/division?A=7/5&B=3/5')
            self.assertEqual(b'2.33333333333333', rv.data)
        def test_divneg(self):
            rv =  self.app.get('/division?A=7.5&B=-2.5')
            self.assertEqual(b'-3 \n', rv.data)
        
            
if __name__ == '__main__':
    unittest.main()
