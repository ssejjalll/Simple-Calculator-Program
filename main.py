def calculator():
    # Welcome message
    print("Welcome to the Simple Calculator.")

    while True:
        # Get user input for two numbers
        num1_str = input("Enter the first number (or 'q' to quit): ")
        if num1_str.lower() == 'q':
            print("Thank you for using the Simple Calculator. Goodbye!")  # Confirmation message
            break  # Exit the loop if the user enters 'q'

        if not num1_str.replace('.', '', 1).isdigit():
            print("Invalid input. Please enter a valid number.")
            continue  # Go to the next iteration of the loop

        num2_str = input("Enter the second number: ")
        if not num2_str.replace('.', '', 1).isdigit():
            print("Invalid input. Please enter a valid number.")
            continue

        num1 = float(num1_str)
        num2 = float(num2_str)

        # Get user input for the operation
        operation = input("Enter an operation (+, -, *, /): ")

        # Perform the calculation based on the operation
        if operation == "+":
            result = num1 + num2
            print(f"The result of {num1} + {num2} is {result:.2f}")
        elif operation == "-":
            result = num1 - num2
            print(f"The result of {num1} - {num2} is {result:.2f}")
        elif operation == "*":
            result = num1 * num2
            print(f"The result of {num1} * {num2} is {result:.2f}")
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
                print(f"The result of {num1} / {num2} is {result:.2f}")
            else:
                print("Error! Division by zero.")
        else:
            print("Invalid operation! Please enter one of the following: +, -, *, /")

# Start Calculator
calculator()