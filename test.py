import unittest

import rsaidnumber


def id_number():
    number = rsaidnumber.parse('9903105047084')
    return number.valid


class Rsa(unittest.TestCase):
    def checking(self):
        a = rsaidnumber.parse('9903105047084')

    def testing(self):
        self.assertTrue(rsaidnumber.RSA_ID_LENGTH, 13)


if __name__ == '__main__':
    unittest.main()
