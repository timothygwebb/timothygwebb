import unittest
"""Module has a function that prints the name of my site"""


def print_site_name():
    """Function printing the name of my site"""
    site = 'github.com/timothygwebb'

    print(site)

class TestBasicFunctionality(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(1 + 1, 2)

if __name__ == '__main__':
    unittest.main()
