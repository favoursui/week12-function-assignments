"""
    Task 9:
    Write a function that accepts a word as a parameter
    and returns the number of vowels (a, e, i, o, u) in the word.
    Example: count_vowels("apple") → 2
"""
vowels = ("Aa,Ee,Ii,Oo,Uu")
vowel_count = 0

def vowel_counts(word):
	return vowel_count
words = input("enter a word to count vowels: ")
for char in words:
	if char in vowels:
		vowel_count += 1
count = f"found a total of {vowel_counts(vowel_count)} vowels in '{words}'"
print(count)	










































