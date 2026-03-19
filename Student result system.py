def calculate_grade(percentage):
    if percentage >= 75:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "Fail"

def main():
    print("===== Student Result System =====")

    name = input("Enter student name: ")
    subjects = int(input("Enter number of subjects: "))

    total = 0

    for i in range(subjects):
        while True:
            try:
                marks = float(input(f"Enter marks for subject {i+1}: "))
                if 0 <= marks <= 100:
                    total += marks
                    break
                else:
                    print("Enter marks between 0 and 100")
            except:
                print("Invalid input! Enter numeric value")

    percentage = total / subjects
    grade = calculate_grade(percentage)

    print("\ns===== RESULT =====")
    print("Name:", name)
    print("Total Marks:", total)
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)

    if grade == "Fail":
        print("Status: FAIL")
    else:
        print("Status: PASS")

# Run program
main()