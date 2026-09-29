mark = int(input("Please enter your mark (0-100): "))

if 90 <= mark <= 100:
    grade = "A"
elif 80 <= mark <= 89:
    grade = "B"
elif 70 <= mark <= 79:
    grade = "C"
elif 60 <= mark <= 69:
    grade = "D"
else:
    grade = "E"

print("Grade:", grade)
