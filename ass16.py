"""
    Task 16:
    Write a function that accepts a number and returns its factorial
    using a loop (not recursion).
    Example: factorial(5) → 120
"""

def factorial(number):
	num = 1
	while True:
		if number > 0:
			num *= number
			number -= 1
		return num	



print(factorial(5))		
			















































