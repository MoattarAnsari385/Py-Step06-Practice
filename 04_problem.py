# Write a program to whether a given username contains less than 10 char or not.

user_input = input('Enter a username: ')

if(len(user_input) < 10):
    print('Username is too short')
else:
    print('Username is valid')