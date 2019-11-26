from LinkedList import LinkedList, LinkedNode

class Queue(LinkedList):
	def __init__(self):
		super().__init__()
		self.last_node = self.first_node

	def enqueue(self, item):
		new_last_node = LinkedNode(item)

		if self.last_node:
			self.last_node.link = new_last_node
		else:
			self.first_node = new_last_node

		self.last_node = new_last_node

	def is_empty(self):
		return self.first_node == None

if __name__ == '__main__':
	my_queue = Queue()
	my_queue.enqueue(1)
	my_queue.enqueue(2)
	my_queue.enqueue(3)	

	print_node = my_queue.return_head()
	print("My queue, top to bottom")
	while print_node:
		print(print_node.data)
		print_node = print_node.link

	my_queue.pop()
	print("Removed one")
	print_node = my_queue.return_head()
	print("My queue, top to bottom")
	while print_node:
		print(print_node.data)
		print_node = print_node.link
	
	my_queue.pop()
	print("Removed one")
	print_node = my_queue.return_head()
	print("My queue, top to bottom")
	while print_node:
		print(print_node.data)
		print_node = print_node.link

	my_queue.pop()
	print("Removed one. Should be empty now")
	print(my_queue.is_empty())

#first in first out
# enqueue adds to bottom - need a way to track the last item
# dequeue removes from top - use super.pop()
# peek returns the first element - use super.return_head()
# is_empty
