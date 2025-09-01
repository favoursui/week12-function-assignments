"""
    Task 21:
    Write a function that works like a simple calculator.
    It should accept two numbers and an operation (+, -, *, /)
    and return the result.
    Example: calculator(4, 2, "+") → 6
"""

def simple_calculator(a, b, operator):	
	if operator == "+":
		return a+b
	elif operator == "-":
		return a-b
	elif operator == "*":
		return a*b
	elif operator == "/":
		if b != 0:
			return a/b
		else:
			return "zero division error"
	else:
		return "invalid operator"		 

		
print(simple_calculator(5, 0, "/"))








