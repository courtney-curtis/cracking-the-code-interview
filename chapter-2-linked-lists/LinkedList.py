class LinkedNode:
    def __init__(self, data, link = None):
        self.data = data
        self.link = link

    def link_next_node(self, next_node):
        self.link = next_node
    
class LinkedList:
    def __init__(self, first_node):
        self.first_node = first_node

    def insert_new_first_node(self, new_element_data):
        new_node = LinkedNode(new_element_data, self.first_node)
        self.first_node = new_node

    def remove_first_node(self):
        new_first_node = self.first_node.link

def remove_dupes(linked_list):
    check_dict = {}
    this_node = linked_list.first_node
    prev_node = None

    while this_node:
        if this_node.data in check_dict:
            prev_node.link = this_node.link
        else:
            check_dict[this_node.data] = True
        prev_node = this_node
        this_node = this_node.link

    print_node = linked_list.first_node
    while print_node:
        print(print_node.data)
        print_node = print_node.link
        
    return linked_list

if __name__ == '__main__':
    node_4 = LinkedNode(3)
    node_3 = LinkedNode(3, node_4)
    node_2 = LinkedNode(2, node_3)
    node_1 = LinkedNode(1, node_2)

    linked_list = LinkedList(node_1)
    remove_dupes(linked_list)
        
#characteristics
# insert an element at the front
# delete an item from the front
# return the head of the list
