try:
    mark = int(input("Enter your mark (0-100): "))

    if mark < 0 or mark > 100:
        print("Error: Mark must be between 0 and 100.")
    elif 90 <= mark <= 100:
        print("Grade: A")
    elif 80 <= mark <= 89:
        print("Grade: B")
    elif 70 <= mark <= 79:
        print("Grade: C")
    elif 60 <= mark <= 69:
        print("Grade: D")
    else:
        print("Grade: E")

except ValueError:
    print("Error: Please enter a valid whole number.")
