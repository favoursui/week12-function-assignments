"""
    Task 14:
    Write a function that accepts a list of numbers
    and returns the sum of all the elements in the list.
    Do not use Python's built-in sum() function.
"""
def num_list(numbers):
	add = 0	
	for num in numbers:
		add += num
	return add
print(num_list([1,2,3,4]))

















































