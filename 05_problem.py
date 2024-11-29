# Write a program to find out whether a given name is present in a list or not.

user_input = input("Enter name here: ")
person = ["maryam", "moattar", "manal", "khazina", "aroob", "fatima", "anoshay"]

if user_input.lower() in person:
    print(f"{user_input} is present in the list.")
else:
    print(f"{user_input} is not present in the list.")