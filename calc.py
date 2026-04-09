def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")
def calaculator():
    while True:
        print("Calculator")
        print("Enter 'exit' if you want to quit from Calculator")
        num1 = input("Enter first number: ")
        if num1.lower() == 'exit':
            print("Exiting Calculator!! Good Byee..")
            break
        operator = input("Enter opeartion: ")
        if operator.lower() == 'exit':
            print("Exiting Calculator!! Good Byee..")
            break
        num2 = input("Enter second number: ")
        if num2.lower() == 'exit':
            print("Exiting Calculator!! Good Byee..")
            break

        num1 = float(num1)
        num2 = float(num2)

        if operator == '+':
            print("The addition of ", num1," and ", num2, " is ", add(num1, num2))
        elif operator == '-':
            print("The substraction of ", num1," and ", num2, " is ", sub(num1, num2))
        elif operator == '*':
            print("The multiplication of ", num1," and ", num2, " is ", mul(num1, num2))
        elif operator == '/':
            print("The division of ", num1," and ", num2, " is ", div(num1, num2))
        else:
            print("Invalid operation Please choose from +,-,*,/.")

calaculator()
