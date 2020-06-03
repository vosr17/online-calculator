import main
import unittest

class MyTestCase(unittest.TestCase):

        def setUp(self):
            main.app.testing = True
            self.app = main.app.test_client()

        def test_addint(self):
            rv =  self.app.get('/addition?A=7&B=6')
            self.assertEqual(b'13 \n', rv.data)
            self.assertNotEqual(b'6.000 \n',rv.data)
        def test_addfloat(self):
            rv =  self.app.get('/addition?A=7.5&B=2.5')
            self.assertEqual(b'10 \n', rv.data)
        def test_addfrac(self):
            rv =  self.app.get('/addition?A=7/5&B=3/5')
            self.assertEqual(b'2 \n', rv.data)
            self.assertNotEqual(b'3.6 \n',rv.data)
        def test_addneg(self):
            rv =  self.app.get('/addition?A=7.5&B=-2.5')
            self.assertEqual(b'5 \n', rv.data)
        
            
if __name__ == '__main__':
    unittest.main()
