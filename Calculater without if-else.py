# Define operation functions
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b if b != 0 else "Cannot divide by zero"

# Operation map using dictionary
operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div
}
# User input
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Get and execute the operation, or show error
result = operations.get(operator, lambda a, b: "Invalid operator")(num1, num2)

# Output
print("Result:", result)
