import unittest
from passwdMd5 import login


class TestLogin(unittest.TestCase):
    def test_something(self):
        self.assertEqual(login('alice', 'alice2008'), True)


if __name__ == '__main__':
    unittest.main()
