# Write a program to find out whether a given post is talking about "Moattar" or not.
post = input("Give your feedback").lower()

if ("Mooattar Ansari".lower() in post):
    print("The post is talking about Moattar Ansari.")
else:
    print("The post is not talking about Moattar Ansari.")