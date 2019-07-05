import unittest
from LinkedListDS.LinkedList import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_init(self):
        linkedlist = LinkedList()
        self.assertEqual(None, linkedlist.head)
        self.assertEqual(0, linkedlist.counter)

    def test_operation(self):
        linkedlist = LinkedList()
        # self.assertEqual(True, linkedlist.insert_start(12))
        # self.assertEqual(True, linkedlist.insert_start(7))
        # self.assertEqual(True, linkedlist.insert_start(2))
        # self.assertEqual(True, linkedlist.insert_end(1))
        # self.assertEqual(2, linkedlist.head.data)
        # self.assertEqual(4, linkedlist.size())
        # self.assertEqual(True, linkedlist.remove(12))
        # self.assertEqual(3, linkedlist.size())
        # self.assertEqual(False, linkedlist.remove(62))
        # self.assertEqual(3, linkedlist.size())
        self.assertEqual(False, linkedlist.remove(12))
        self.assertEqual(True, linkedlist.insert_end(12))
        self.assertEqual(12, linkedlist.head.data)
        self.assertEqual(1, linkedlist.size())


if __name__ == '__main__':
    unittest.main()
