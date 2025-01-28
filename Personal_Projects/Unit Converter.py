import math 

def pounds_to_kilos(a):
    return a * 0.45359237

def kilos_to_pounds(a):
    return a * 2.205

def celsius_to_fahrenheit(a):
    return (a * 9/5)+32

def fahrenheit_to_celsius(a):
    return (a-32)*5/9

def meters_to_cm(a):
    return a * 100 

def cm_to_meters(a):
    return a/100

def converter():
    while True:
        print("\nWelcome to the converter")
        print("1. Pounts to Kilos")
        print("2. Kilos to pounds")
        print("3. Celsius to Fahrenheit")
        print("4. Fahrenheit to Celsius")
        print("5. meters to Centimeters")
        print("6. Centimeters to meters")
        print("7. Exit")

        choice = (input(print("Welcome! choose a coverter")))

        if choice == "7":
            print("Goodbye!")
            break
        elif choice == "1":
            try:
                pounds = float(input(print("Enter pounds: ")))
                print(f"Kilos: {pounds_to_kilos(pounds)}")
            except ValueError:
                print("invalid Input")
        
        elif choice == "2":
            try:
                kilos = float(input(print('Enter a value in kilos: ')))
                print(f"Pounds: {kilos_to_pounds(kilos)}")
            except ValueError:
                print("Invalid Input")
        elif choice == "3":
            try:
                celsius = float(input(print("Enter a temperature in celsius: ")))
                print(f"Fahrenheit: {celsius_to_fahrenheit(celsius)}")
            except ValueError:
                print("Invalid Input")
        elif choice == "4":
            try:
                Fahrenheit = float(input(print("Enter a value in Fahrenheit: ")))
                print(f"Celsius: {fahrenheit_to_celsius(Fahrenheit)}")
            except ValueError:
                print("Invalid Input")
        elif choice == "5":
            try:
                meters = float(input(print("Enter a length in meters: ")))
                print(f"Centimeters: {meters_to_cm(meters)}")  
            except ValueError:
                print("Invalid Input") 
        elif choice == "6":
            try:
                centimeters = float(input(print("Enter a value in CM: "))) 
                print(f"Meters: {cm_to_meters(centimeters)}") 
            except ValueError:
                print("Invalid Input")
        else:
            print("Invalid Input") 
converter()          