def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
print("Simple Calculator")
print("Basic Arithmetic operations are:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = int(input("Enter operation choice (1/2/3/4): "))

if operation == 1:
    result = add(num1, num2)
    print("Result is:", result)
elif operation == 2:
    result = subtract(num1, num2)
    print("Result is:", result)
elif operation == 3:
    result = multiply(num1, num2)
    print("Result is:", result)
elif operation == 4:
    result = divide(num1, num2)
    print("Result is:", result)
else:
    print("Invalid operation choice.")
