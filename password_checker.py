password = input("Enter your password: ")

if len(password) < 8:
    print("Weak password")
elif password.isalpha() or password.isdigit():
    print("Password needs letters and numbers")
else:
    print("Password length and character mix look better")
