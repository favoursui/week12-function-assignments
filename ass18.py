"""
    Task 18:
    Write a function that accepts minutes as input
    and converts it into hours and minutes.
    Example: 130 minutes → "2 hour(s) 10 minute(s)"
"""

def minute_convert(convert):
	hour = time // 60
	minutes = time % 60
	return hour, minutes
time = int(input("enter time in minute to convert: "))	
hour, minutes = minute_convert(time)
print(f"{time}min(s) = {hour}hr(s) {minutes}min(s)")













































