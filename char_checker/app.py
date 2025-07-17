print("CHARACTER CHECKER")
char = input("Enter a single character:\n")
if char.isalpha():
    print("This is a letter.")
elif char.isdigit():
    print("This is a digit.")
else:
    print("This is a special character.")


    