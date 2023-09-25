# Import the math module to access mathematical functions
import math

# Define a function for adding two numbers
def add(x, y):
    return x + y

# Define a function for subtracting one number from another
def subtract(x, y):
    return x - y

# Define a function for multiplying two numbers
def multiply(x, y):
    return x * y

# Define a function for dividing one number by another, with handling for division by zero
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Define a function for calculating the square root of a number
def square_root(x):
    if x < 0:
        return "Invalid input"
    return math.sqrt(x)

# Define a function for calculating the result of raising one number to the power of another
def power(x, y):
    return x ** y

# Define a function for calculating the factorial of a number
def factorial(x):
    if x < 0:
        return "Invalid input"
    if x == 0:
        return 1
    return math.factorial(x)

# Define a function for calculating the average of a list of numbers
def calculate_average(numbers):
    if len(numbers) == 0:
        return "List is empty"
    return sum(numbers) / len(numbers)

# Define a function for calculating the percentage of one number relative to another
def calculate_percentage(x, y):
    if y == 0:
        return "Cannot calculate percentage with denominator zero"
    return (x / y) * 100

# Create an infinite loop to keep the program running until the user chooses to quit
while True:
    # Display a list of available options to the user
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'sqrt' for square root")
    print("Enter 'power' for exponentiation")
    print("Enter 'factorial' for factorial")
    print("Enter 'average' for calculating average")
    print("Enter 'percentage' for calculating percentage")
    print("Enter 'quit' to end the program")

    # Prompt the user for their choice
    user_input = input(": ")

    # Check if the user wants to quit the program
    if user_input == "quit":
        break
    # Check if the user's input matches one of the available mathematical operations
    elif user_input in ("add", "subtract", "multiply", "divide", "sqrt", "power", "factorial"):
        try:
            # Prompt the user for input numbers
            num1 = float(input("Enter first number: "))
            # Check if the selected operation is square root or factorial
            if user_input in ("sqrt", "factorial"):
                if user_input == "sqrt":
                    # Calculate and print the result of the square root operation
                    print("Result:", square_root(num1))
                else:
                    # Calculate and print the result of the factorial operation
                    print("Result:", factorial(int(num1)))
            else:
                # For other operations (add, subtract, multiply, divide, power), prompt for a second number
                num2 = float(input("Enter second number: "))
                # Perform the selected operation and print the result
                if user_input == "add":
                    print("Result:", add(num1, num2))
                elif user_input == "subtract":
                    print("Result:", subtract(num1, num2))
                elif user_input == "multiply":
                    print("Result:", multiply(num1, num2))
                elif user_input == "divide":
                    print("Result:", divide(num1, num2))
                elif user_input == "power":
                    print("Result:", power(num1, num2))
        except ValueError:
            # Handle invalid input by displaying an error message
            print("Invalid input. Please enter valid numbers.")
    # Check if the user's input matches the average or percentage operations
    elif user_input in ("average", "percentage"):
        num_list = []
        while True:
            # Prompt the user for a series of numbers or "done" to finish
            num = input("Enter a number (or 'done' to finish): ")
            if num.lower() == 'done':
                break
            try:
                # Convert the input to a float and append it to the list
                num_list.append(float(num))
            except ValueError:
                # Handle invalid input by displaying an error message
                print("Invalid input. Please enter a valid number.")
        
        if user_input == "average":
            # Calculate and print the average of the entered numbers
            print("Result:", calculate_average(num_list))
        elif user_input == "percentage":
            # Check if there are at least two numbers to calculate the percentage
            if len(num_list) < 2:
                print("At least two numbers are required to calculate a percentage.")
            else:
                # Calculate and print the percentage
                x = num_list[0]
                y = num_list[1]
                print("Result:", calculate_percentage(x, y))
    else:
        # Handle invalid input by displaying an error message
        print("Invalid input")
