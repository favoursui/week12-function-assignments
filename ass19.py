"""
    Task 19:
    Write a function that accepts a list of numbers
    and returns the smallest number.
    Do not use Python's built-in min() function.
"""
def min_num(numbers):
	small = numbers[0]
	for num in numbers:
		if num < small:
			small = num
	return small
print(min_num([10, 2, 3, 51, 4, 100, 21]))	

	











































