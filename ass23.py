"""
    Task 23:
    Write a function that accepts a score (0–100)
    and returns the grade based on this scale:
    A: 70–100
    B: 60–69
    C: 50–59
    D: 40–49
    E: 30–39
    F: 0–29
"""
def grade_student(score):
	if score >= 70 and score <= 100:
		return "A"
	elif score >= 60 and score <= 69:
		return "B"
	elif score >= 50 and score <= 59:
		return "C"
	elif score >= 40 and score <= 49:
		return "D"
	elif score >= 30 and score <= 39:
		return "E"
	elif score >= 0 and score <= 29:
		return "F"
	else:
		return "invalid score"						

print(grade_student(67))		





































