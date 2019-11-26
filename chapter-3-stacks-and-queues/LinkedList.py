class LinkedNode:
	def __init__(self, data, link = None):
		self.data = data
		self.link = link

	def link_next_node(self, next_node):
		self.link = next_node
    
class LinkedList:
	def __init__(self, first_node=None):
        	self.first_node = first_node

	def push(self, new_element_data):
		new_node = LinkedNode(new_element_data, self.first_node)
		self.first_node = new_node

	def pop(self):
		old_first_node = self.first_node
		new_first_node = self.first_node.link
		self.first_node = new_first_node
		return old_first_node

	def return_head(self):
		return self.first_node

#characteristics
# insert an element at the front
# delete an item from the front
# return the head of the list
