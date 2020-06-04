import main
import unittest

class MyTestCase(unittest.TestCase):

        def setUp(self):
            main.app.testing = True
            self.app = main.app.test_client()

        def test_mulint(self):
            rv =  self.app.get('/multiplication?A=7&B=6')
            self.assertEqual(b'42 \n', rv.data)
        def test_mulfloat(self):
            rv =  self.app.get('/multiplication?A=7.5&B=2.5')
            self.assertEqual(b'18.75', rv.data)
        def test_mulfrac(self):
            rv =  self.app.get('/multiplication?A=7/5&B=3/5')
            self.assertEqual(b'0.84', rv.data)
        def test_mulneg(self):
            rv =  self.app.get('/multiplication?A=7.5&B=-2.5')
            self.assertEqual(b'-18.75', rv.data)
        
            
if __name__ == '__main__':
    unittest.main()
