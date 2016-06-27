import unittest

from backend import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.create_app(debug=True)
        self.app.config['TESTING'] = True

    def test_test(self):
        from backend.app import worker
        pass


if __name__ == '__main__':
    unittest.main()