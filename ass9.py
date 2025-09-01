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
word = input("enter a word: ")	
for char in word:
	if char in vowels:
		vowel_count += 1
print(f"found {vowel_counts(vowel_count)} vowels in {word}")









































