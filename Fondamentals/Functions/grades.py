def grade_func(grades):
    result=""
    if 2 <= grades <= 2.99:
        result = "Fail"
    elif 3.00 <= grades <= 3.49:
        result = "Poor"
    elif 3.50 <= grades <= 4.49:
        result = "Good"
    elif 4.50 <= grades <= 5.49:
        result = "Very Good"
    elif 5.50 <= grades <= 6.00:
        result = "Excellent"
    return result


grade=float(input())
print(grade_func(grade))
