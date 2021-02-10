import unittest

import BST, Stack, Queue, Node
# TODO(choisehyun): make test cases for others too.


class CustomTests(unittest.TestCase):
    """Tests of the custom datastrs."""
    def test_runs(self):
        """basics test runs."""
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
