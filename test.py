from main import substraction
import main
import unittest


class TestOnlineCalculator(unittest.TestCase):
    """Testing features of substraction in online calculator"""

    def setUp(self):
        """Sets up the app for testing"""
        main.app.testing = True
        self.app = main.app.test_client()

    def test_substraction(self):
        """Tests page with /sub route, testing substraction feature of the calculator,
        right now all types of numbers being tested"""

        # integer numbers testing
        response_data = self.app.get('/sub?A=34&B=30')
        self.assertEqual(b'4 \n', response_data.data)

        # rational numbers testing
        response_data = self.app.get('/sub?A=2/3&B=3/7')
        self.assertEqual(b'0.23809523809524', response_data.data)

        # when both A and B are both floats
        response_data = self.app.get('/sub?A=5.4&B=3.4')
        self.assertEqual(b'2 \n', response_data.data)

        # when A is an int and B is float
        response_data = self.app.get('/sub?A=8&B=1.234')
        self.assertEqual(b'6.766', response_data.data)

        # when A is a float and B is an int
        response_data = self.app.get('/sub?A=-5.35&B=2')
        self.assertEqual(b'-7.35', response_data.data)

        # when A is a fraction and B is an int
        response_data = self.app.get('/sub?A=4/5&B=3')
        self.assertEqual(b'-2.2', response_data.data)

        # when A is an int and B is a fraction
        response_data = self.app.get('/sub?A=7&B=5/6')
        self.assertEqual(b'6.16666666666667', response_data.data)

        # corner cases testing
        # when A = x/0 where x belongs to integer
        response_data = self.app.get('/sub?A=-1/0&B=7/9')
        self.assertEqual(b"A's denominator should not be zero! \n", response_data.data)

        # when B = x/0 where x belongs to integer
        response_data = self.app.get('/sub?A=-4&B=1000/0')
        self.assertEqual(b"B's denominator should not be zero! \n", response_data.data)

if __name__ == '__main__':
    unittest.main()