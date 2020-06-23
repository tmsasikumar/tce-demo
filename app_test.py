
import unittest

from app import addNums


class BasicUnitTests(unittest.TestCase):
    def testAddNums(self):
        expectedOutput = addNums(10, 25)
        self.assertEqual(expectedOutput, "35")

if __name__ == "__main__":
    unittest.main()

