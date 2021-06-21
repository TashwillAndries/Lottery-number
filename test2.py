import unittest

def Winnings():
    earnings1 = 20
    earnings2 = 20
    earnings3 = 10
    winnings = earnings1 + earnings2 + earnings3
    print(winnings)
    return winnings


# checking if the function runs
class AddingWinnings(unittest.TestCase):
    def adding(self):
        results = Winnings()
        self.assertEqual(results, 60)


if __name__ == '__main__':
    unittest.main()
