import main
import unittest

class MyTestCase(unittest.TestCase):

        def setUp(self):
            main.app.testing = True
            self.app = main.app.test_client()

        def test_subint(self):
            rv =  self.app.get('/substraction?A=7&B=6')
            self.assertEqual(b'1 \n', rv.data)
        def test_subfloat(self):
            rv =  self.app.get('/substraction?A=7.5&B=2.5')
            self.assertEqual(b'5 \n', rv.data)
        def test_subfrac(self):
            rv =  self.app.get('/substraction?A=7/5&B=3/5')
            self.assertEqual(b'0.8', rv.data)
        def test_subneg(self):
            rv =  self.app.get('/substraction?A=7.5&B=-2.5')
            self.assertEqual(b'10 \n', rv.data)
        
            
if __name__ == '__main__':
    unittest.main()
