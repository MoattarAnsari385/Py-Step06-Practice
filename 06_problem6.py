# Write a program to calculate the grade of student from his marks from the following scheme.

uset_input = int(input("Enter your marks: "))

if(uset_input <= 100 and uset_input >= 90):
    print("Grade: Ex")
elif(uset_input < 90 and uset_input >= 80):
    print("Grade: A")
elif(uset_input < 80 and uset_input >= 70):
    print("Grade: B")
elif(uset_input < 70 and uset_input >= 60):
    print("Grade: C")
elif(uset_input < 60 and uset_input >= 50):
    print("Grade: D")
else:
    print("Grade: F")
