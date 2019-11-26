class ThreeStackArray:
	def __init__(length):
		my_stacks = []
		self.stack_one_head = 0
		self.stack_two_head = length/3
		self.stack_three_head = (2*length)/3
	
	def is_full(stack):
		end_of_stack = ((stack*length) / 3) - 1
		
		try my_stacks[end_of_stack]:
			return True
		except:
			return False

	def is_empty(stack):
		stack_bottom = (stack-1)*(len/3)
		
		try my_stacks[stack_bottom]:
			return False
		except:
			return True
	
#pop
#push
#peek
#is_empty
