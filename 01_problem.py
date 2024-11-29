# Write a program to find the greatest number of four numbers entered by the user

a1 = int(input("Enter a number1 here: "))
a2 = int(input("Enter a number2 here: "))
a3 = int(input("Enter a number3 here: "))
a4 = int(input("Enter a number4 here: "))

if a1 > a2 and a1 > a3 and a1 > a4:
    print(f"the greatest number is a1 {a1}")
elif a2 > a1 and a2 > a3 and a2 > a4:
    print(f"the greatest number is a2 {a2}")
elif a3 > a1 and a3 > a2 and a3 > a4:
    print(f"the greatest number is a3 {a3}")
else:
    print(f"The greatest number is a4 {a4}")

