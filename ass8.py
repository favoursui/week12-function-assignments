"""
    Task 8:
    Write a function that accepts a number and returns
    "Even" if the number is even, and "Odd" if the number is odd.
"""


def start():
	while True:
		num = int(input("enter a number: "))
		even(num)
		odd(num)

def even(num):
	if num % 2 == 0:
		print("even number")


def odd(num):
	if num % 2 != 0:
		print("odd number")



start()		


















































