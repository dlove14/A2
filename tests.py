import unittest
import string
from check_pwd import check_pwd


class TestCase(unittest.TestCase):

    def test1(self):
        pwd = "525225"
        self.assertFalse(check_pwd(pwd), "error")

    def test2(self):
        pwd = "ADBCHEDJID"
        self.assertFalse(check_pwd(pwd), "error")

    def test3(self):
        pwd = "fahfkbaffawfaw"
        self.assertFalse(check_pwd(pwd), "error")

    def test4(self):
        pwd = "qqfqwfwwqeqwqe"
        self.assertFalse(check_pwd(pwd), "error")

    def test5(self):
        pwd = "dfqwfAwfqw2"
        self.assertFalse(check_pwd(pwd), "error")


if __name__ == '__main__':
    unittest.main()
