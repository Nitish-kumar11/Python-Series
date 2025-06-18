email = input("Enter your email: ")

if " " in email:
    print("Its Invalid Email: contains space")
elif "@" in email and "." in email:
    at_index = email.index("@")
    dot_index = email.rindex(".")
    if at_index < dot_index:
        print("Valid Email")
    else:
        print("Invalid Email: '.' should come after '@'")
else:
    print("Invalid Email: Missing '@' or '.'")
