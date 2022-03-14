a = int(input("Number of Classes Held: "))

b = int(input("Number of Classes Attended: "))

Percentage = b / a * 100  # finding percentage

if Percentage >= 75:

    print("The Student is ALLOWED to Sit in Exam_hall")

else:

    print("The Student is NOT ALLOWED to Sit in Exam_hall")