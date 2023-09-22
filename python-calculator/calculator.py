import math


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y


def square_root(x):
    if x < 0:
        return "Invalid input"
    return math.sqrt(x)


def power(x, y):
    return x ** y


def factorial(x):
    if x < 0:
        return "Invalid input"
    if x == 0:
        return 1
    return math.factorial(x)


def calculate_average(numbers):
    if len(numbers) == 0:
        return "List is empty"
    return sum(numbers) / len(numbers)


def calculate_percentage(x, y):
    if y == 0:
        return "Cannot calculate percentage with denominator zero"
    return (x / y) * 100


while True:
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

    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input in ("add", "subtract", "multiply", "divide", "sqrt", "power", "factorial"):
        if user_input in ("sqrt", "factorial"):
            num = float(input("Enter a number: "))
            if user_input == "sqrt":
                print("Result: " + str(square_root(num)))
            else:
                print("Result: " + str(factorial(int(num))))
        else:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if user_input == "add":
                print("Result: " + str(add(num1, num2)))
            elif user_input == "subtract":
                print("Result: " + str(subtract(num1, num2)))
            elif user_input == "multiply":
                print("Result: " + str(multiply(num1, num2)))
            elif user_input == "divide":
                print("Result: " + str(divide(num1, num2)))
            elif user_input == "power":
                print("Result: " + str(power(num1, num2)))
    elif user_input in ("average", "percentage"):
        num_list = []
        while True:
            num = input("Enter a number (or 'done' to finish): ")
            if num.lower() == 'done':
                break
            try:
                num_list.append(float(num))
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        if user_input == "average":
            print("Result: " + str(calculate_average(num_list)))
        elif user_input == "percentage":
            if len(num_list) < 2:
                print("At least two numbers are required to calculate a percentage.")
            else:
                x = num_list[0]
                y = num_list[1]
                print("Result: " + str(calculate_percentage(x, y)))
    else:
        print("Invalid input")