"""
Task 6:
Write a function that converts a temperature from Celsius to Fahrenheit.
Formula: (celsius * 9/5) + 32
"""

def task6_celsius_to_fahrenheit(celsius):
	return (celsius * 9/5) + 32
temperature = float(input("enter a temperature in celcius: "))
fahrenheit = task6_celsius_to_fahrenheit(temperature)
print(f"temperature {temperature}C to Fahrenheit is: {fahrenheit}F")
	








































