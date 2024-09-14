import unittest
import requests

class TestStringMethods(unittest.TestCase):

    def test_statuscode(self):
        res = requests.get("http://localhost:8000").status_code
        # print(dir(res))
        # print(res)
        self.assertEqual(int(res), 200)


if __name__ == '__main__':
    unittest.main()
