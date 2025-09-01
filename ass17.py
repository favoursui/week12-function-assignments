"""
    Task 17:
    Write a function that checks if a word is a palindrome.
    A palindrome reads the same forwards and backwards.
    Example: palindrome_check("madam") → True
"""

def palindrome(word):
	if word == word[::-1]:
		return True
	else:
		return False
print(palindrome("madam"))			
	











































