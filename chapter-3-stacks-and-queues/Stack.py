from LinkedList import LinkedList

class Stack(LinkedList):
	def is_empty(self):
		if None == self.return_head():
			return True
		else:
			return False

	def get_size(self):
		size_counter = 0
		this_item = self.return_head()
		prev_item = None

		while this_item:
			size_counter += 1
			this_item = this_item.link

		return size_counter

if __name__ == '__main__':
	my_stack = Stack()
	print("Push 1")
	my_stack.push(1)
	print("Push 2")
	my_stack.push(2)
	print("Push 3")
	my_stack.push(3)
	print("Print stack")	
	print_node = my_stack.return_head()
	while print_node:
		print(print_node.data)
		print_node = print_node.link
	print("Print size of stack")
	print(my_stack.get_size())
	print("Removed an item")
	my_stack.pop()
	print_node = my_stack.return_head()
	while print_node:
		print(print_node.data)
		print_node = print_node.link
	print("Removed an item")
	my_stack.pop()
	print_node = my_stack.return_head()
	while print_node:
		print(print_node.data)
		print_node = print_node.link
	print("Removed an item. The list should be empty now")
	my_stack.pop()
	print(my_stack.is_empty())

#last in first out
#push item onto stack -- super.push()
#return top item of stack -- super.return_head()
#pop top item out of stack -- super.pop()
#is-empty
#is-full
#get-size
