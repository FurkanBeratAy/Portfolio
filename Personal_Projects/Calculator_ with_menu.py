import math 

def addition(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0:
        return "Erros division by 0"
    else:
        return a/b
def calculator():
    print("Welcome to the Python Calculator")
    while True:
        print("\nSelect a function")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input(print("Enter your choice (1,2,3,4,5):"))

        if choice == '5':
            print("Goodbye!")
            break 
        if choice in ['1','2','3','4']:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if choice == "1":
                    print(f"The result is: {addition(num1, num2)}")
                elif choice == "2":
                    print(f"The result is: {subtract(num1,num2)}")
                elif choice == "3":
                    print(f"The result is:{multiply(num1,num2)}")
                elif choice == "4":
                    print(f"The result is: {divide(num1,num2)}")
            except  ValueError:
                print("Invalid input please re enter numbers")
        else:
            print("Invalid choice please select a valid option")

calculator()

