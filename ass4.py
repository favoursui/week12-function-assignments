"""
Task 4:
Write a function that accepts the length and width of a rectangle
and returns its area.
Formula: area = length * width
"""


def area_of_rectangle(length, width):
	return length * width
length = float(input("enter the length of your rectangle: "))	
width = float(input("enter the width of your rectangle: "))
area = area_of_rectangle(length, width)
print(f"the area of a rectangle of witdth {width} and length {length} is: {area}")


































