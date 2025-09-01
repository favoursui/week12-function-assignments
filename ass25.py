"""
    Task 25:
    Create a counter function that uses a global variable.
    Each time the function is called, it should increase
    the counter by 1 and print the current count.
    This demonstrates modifying global variables inside functions.
"""
count = 0
def scope_count():
	count += 1
	return count
scope_count()


































