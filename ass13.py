"""
    Task 13:
    Demonstrate local and global scope.
    Create a global variable, and then inside a function,
    create a local variable with the same name. Print both
    to show how local and global scope works.
"""

vowels = "aeiou"
count = 0
def vowel_count():
    global count
    words = input("enter a word to count vowels: ")
    for char in words:
        if char in vowels:
            count += 1
    print(count)
vowel_count()			








































