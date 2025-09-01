"""
    Task 15:
    Write a function that accepts a list of numbers
    and returns the average.
    Formula: average = sum of numbers / count of numbers
"""
def avg_numbers(numbers):
	add = 0
	for num in numbers:
		add += num
	return add / len(numbers)	
print(avg_numbers([1,2,3,4]))	















































