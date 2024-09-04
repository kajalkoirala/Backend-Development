def add(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: Division by zero is undefined."
    else:
        return a / b

def get_user_input():
    # Loop until a valid operator is entered
    while True:
        operation = input("Choose operator (+, -, *, /): ")
        if operation in ('+', '-', '*', '/'):
            break  # Exit loop if the operator is valid
        print("Invalid operator! Please use one of +, -, *, /.")
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return operation, num1, num2
    except ValueError:
        print("Invalid input! Please use numeric values.")
        return None

def calculation():
    user_input = get_user_input()

    if user_input is None:
        return
    
    operation, num1, num2 = user_input
    
    if operation == '+':
        print(f"Result: {add(num1, num2)}")
    elif operation == '-':
        print(f"Result: {subtraction(num1, num2)}")
    elif operation == '*':
        print(f"Result: {multiplication(num1, num2)}")
    elif operation == '/':
        print(f"Result: {division(num1, num2)}")

if __name__ == "__main__":
    calculation()
