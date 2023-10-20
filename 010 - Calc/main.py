import logo


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multipy(a, b):
    return a * b


def divide(a, b):
    return a / b


print(logo.logo)
operations = {
    "+": add,
    "-": subtract,
    "*": multipy,
    "/": divide,
}

calculating = True
num1 = float(input("Please enter your first number: "))

while calculating:
    for symbol in operations:
        print(symbol)

    operation = input("Choose an operation.\n")
    while operation not in operations:
        for symbol in operations:
            print(symbol)
        operation = input("Choose an operation.\n")

    num2 = float(input("Please enter your second number: "))
    result = operations[operation](num1, num2)
    print(f"{num1} {operation} {num2} = {result}")
    another = input(f"Need to calculate further on {result}? y/n\n").lower()
    calculating = True if another in ["y", "yes"] else False
    num1 = result
