def calculator():
    # Welcome message
    print("Welcome to the Simple Calculator.")

# Start Calculator
calculator()

# Get user input for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#Get user input for the operation
operation = input("Enter an operation(+, -, *, /): ")

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
    print("Invalid operation! Please enter one of the +, -, *, /")