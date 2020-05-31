from main import division
import main
import unittest


class TestOnlineCalculator(unittest.TestCase):
    
    """Testing features of division in online calculator"""

    def setUp(self):
        """Sets up the app for testing"""
        main.app.testing = True
        self.app = main.app.test_client()

    def test_division(self):
        """Tests page with /div route, testing division feature of the calculator,
        right now all types of numbers being tested"""

        # integer numbers testing
        response_data = self.app.get('/div?A=3&B=4')
        self.assertEqual(b'0.75', response_data.data)

        # rational numbers testing
        response_data = self.app.get('/div?A=2/3&B=3/7')
        self.assertEqual(b'1.55555555555556', response_data.data)

        # when both A and B are both floats
        response_data = self.app.get('/div?A=5.4&B=3.4')
        self.assertEqual(b'1.58823529411765', response_data.data)

        # when A is an int and B is float
        response_data = self.app.get('/div?A=8&B=1.234')
        self.assertEqual(b'6.48298217179903', response_data.data)

        # when A is a float and B is an int
        response_data = self.app.get('/div?A=-5.35&B=2')
        self.assertEqual(b'-2.675', response_data.data)

        # when A is a fraction and B is an int
        response_data = self.app.get('/div?A=4/5&B=3')
        self.assertEqual(b'0.26666666666667', response_data.data)

        # when A is an int and B is a fraction
        response_data = self.app.get('/div?A=7&B=5/6')
        self.assertEqual(b'8.4', response_data.data)

        # corner cases testing
        # when A = x/0 where x belongs to integer
        response_data = self.app.get('/div?A=-1/0&B=7/9')
        self.assertEqual(b"A's denominator should not be zero! \n", response_data.data)

        # when B = x/0 where x belongs to integer
        response_data = self.app.get('/div?A=-4&B=1000/0')
        self.assertEqual(b"B's denominator should not be zero! \n", response_data.data)

        # when A is a non-number
        response_data = self.app.get('/div?A=x&B=niheeth')
        self.assertEqual(b"A's value should be a number (includes fraction, float, integer). \n", response_data.data)

if __name__ == '__main__':
    unittest.main()