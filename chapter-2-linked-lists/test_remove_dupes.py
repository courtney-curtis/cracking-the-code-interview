import unittest

from LinkedList import LinkedNode, LinkedList
from remove_dupes import remove_dupes

class TestRemoveDupes(unittest.TestCase):
    
    def test_remove_dupes(self):
        test_node_4 = LinkedNode(3)
        test_node_3 = LinkedNode(3, test_node_4)
        test_node_2 = LinkedNode(2, test_node_3)
        test_node_1 = LinkedNode(1, test_node_2)

        test_linked_list = LinkedList(test_node_1)
        removed_dupes = remove_dupes(test_linked_list)
       
        check_list=[]
        node = removed_dupes.first_node
        while node:
            check_list.append(node.data)
            node = node.link    
        self.assertEqual(check_list, [1,2,3]) 

if __name__ == '__main__':
    unittest.main()
