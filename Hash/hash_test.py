"""Test case for Hash datastr."""
import unittest

from Hash import Hash


class HashTest(unittest.TestCase):
    """Test Hash object."""
    def test_behavior(self):
        """Test basic behavior."""
        h = Hash(1423, 197)
        h.insert(55, 'fifty five')
        self.assertEqual((55, 'fifty five'), h.search('fifty five'))
        self.assertEqual((55, 'fifty five'), h.table[808])
        self.assertEqual('A', h.state[808])

        h.insert(1234, 'one two three four')
        self.assertEqual((1234, 'one two three four'),
                         h.search('one two three four'))


if __name__ == "__main__":
    unittest.main()
