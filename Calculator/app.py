def addition(x,y):
     return x+y

def subtraction(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
    if y==0:
        print("ERROR: DivisionError (division by zero)")
    return x/y

def main():

    print("\n*** SIMPLE CALCULATOR ***")
    print("Select operation:\n 1. Addition \n 2. Subtraction\n 3. multiplication\n 4. Division ")

    while True:

        choice=input("\nEnter your choice: ")
        if choice not in ["1","2","3","4"]:
            print("please enter a valid choice (1-4)")
        else:
            break
    try:
        num1=int(input("enter the first number:"))
        num2=int(input("enter the second number: "))
    except ValueError:
        print("enter a valid choice") 
        return

    if choice == "1": 
        print(f"The addition of {num1} and {num2} is {addition(num1,num2)}")
    elif  choice == "2":
        print(f"The subtraction of {num1} and {num2} is {subtraction(num1,num2)}")
    elif choice == "3":
        print(f"The multiplication  of {num1} and {num2} is {multiplication(num1,num2)}")
    elif choice == "4":
        print(f"The division of {num1} and {num2} is {division(num1,num2)}")
    
    again=input("\n Do you want to perform another calculation(y/n):").lower()
    if not again.startswith("y"):
        print("GOODBYE")
        return
    else:
        main()

main()