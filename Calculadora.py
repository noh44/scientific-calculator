import math

History = []

def valores():
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        return a, b 
    except ValueError:
        print("Please, Enter a valid option :))")
        return None, None
    
def onenumber():
    try:
        y = int(input("Enter the number: "))
        return y
    except ValueError:
        print("Please enter a valid number!")
        return None

while True:

    print("------CALCULATOR----")
    print("1. Sum ")
    print("2. Subtract ")
    print("3. Multiply ")
    print("4. Divide ")
    print("5. Square root")
    print("6. Power ")
    print("7. Factorial")
    print("8. Exit ")
    print("9. History")
    print("------CALCULATOR----")

    try:
        option = int(input("Enter one option: "))
    except ValueError:
        print("Pls enter a valid option")
        continue

    if option == 8:
        print("Come back soon pls :()")
        break
    elif option == 1:
        a, b = valores()
        if a is None:
            continue
        result = a + b
        History.append(f"{a} + {b} = {result:.2f}")
        print(f"The result is {result:.2f} :))")

    elif option == 2:
        a, b = valores()
        if a is None:
            continue
        result = a - b
        History.append(f"{a} - {b} = {result:.2f}")
        print(f"The result is {result:.2f} :))")

    elif option == 3:
        a, b = valores()
        if a is None:
            continue
        result = a * b
        History.append(f"{a} * {b} = {result:.2f}")
        print(f"The result is {result:.2f} :))")

    elif option == 4:
        a, b = valores()
        if a is None:
            continue
        if b == 0:
            print("You can't divide by zero!")
            continue
        result = a / b
        History.append(f"{a} / {b} = {result:.2f}")
        print(f"The result is {result:.2f} :))")
    
    elif option == 5:
        y = onenumber()
        if y is None:
            continue
        if y < 0:
            print("Can't do square root of a negative number!")
            continue
        result = math.sqrt(y)
        History.append(f"√{y} = {result:.2f}")
        print(f"The result is {result:.2f}")

    elif option == 6:
        a, b = valores()
        if a is None:
            continue
        result = math.pow(a, b)
        History.append(f"{a} elevado a {b} = {result:.2f}")
        print(f"The result is {result:.2f}")
    
    elif option == 7:
        y = onenumber()
        if y is None:
            continue
        result = math.factorial(y)
        History.append(f"factorial of {y} = {result}")
        print(f"The result is {result}")
    
    elif option == 9:
        if len(History) == 0:
            print("No operations Yet!")
        else:
            print("----HISTORY----")
            for item in History:
                print(item)
            print("---------------")
    else:
        print("Invalid option")