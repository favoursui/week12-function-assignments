"""
    Task 12:
    Write a function that accepts a number as a parameter
    and returns True if the number is prime, otherwise False.
"""
def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print(prime(13)) 


















































