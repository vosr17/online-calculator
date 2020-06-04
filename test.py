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


