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

#characteristics
# insert an element at the front
# delete an item from the front
# return the head of the list
