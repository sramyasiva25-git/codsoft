def calculator():

    print("------ SIMPLE CALCULATOR ------")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    choice = input("Enter your choice (1/2/3/4): ")

    num1 = float(input("Enter the first number: "))

    num2 = float(input("Enter the second number: "))

    if choice == "1":
        result = num1 + num2
        print("Result of Addition:", result)

    elif choice == "2":
        result = num1 - num2
        print("Result of Subtraction:", result)

    elif choice == "3":
        result = num1 * num2
        print("Result of Multiplication:", result)

    elif choice == "4":
        if num2 != 0:
            result = num1 / num2
            print("Result of Division:", result)
        else:
            print("Error: Cannot divide by zero")

    else:
        print("Invalid choice! Please select between 1 to 4")

calculator()