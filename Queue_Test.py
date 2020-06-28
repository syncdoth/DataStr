import unittest

import BST, Stack, Queue, Node


class CustomTests(unittest.TestCase):

    def test_runs(self):
        t = BST()
        t.insert(5)
        t.insert(4)
        t.insert(3)
        t.insert(7)
        t.insert(6)
        self.assertFalse(t.contains(9))
        self.assertEqual(t.find_max(), 7)
        self.assertEqual(t.find_min(), 3)


if __name__ == '__main__':
    unittest.main()
