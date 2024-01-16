import os


def calcold(result):
    print("+\n-\n*\n/")
    operator = (input("pick the operator"))
    if operator not in ["*", "+", "/", "-"]:
        return calcold(result)
    b = int(input("enter the second number"))
    result = performance(result, b, operator)
    ask = input(
        f"if you want to continue with the current value \n which is {result} press 'y' \n To start the new calculator press 'n' ")
    if ask.lower() == "n":
        main()
    else:
        calcold(result)


def calc():
    a = int(input("enter the first number"))
    print("+\n-\n*\n/")
    operator = (input("pick the operator"))

    if operator not in ["*", "+", "/", "-"]:
        return calc()
    b = int(input("enter the second number"))
    result = performance(a, b, operator)
    ask = input(
        f"if you want to continue with the current value \n which is {result} press 'y' \n To start the new calculator press 'n' ")
    if ask.lower() == "n":
        main()
    else:
        calcold(result)


def performance(a, b, operator):
    if operator == "+":
        return add(a, b)
    elif operator == "-":
        return sub(a, b)
    elif operator == "*":
        return mul(a, b)
    elif operator == "/":
        return div(a, b)


def add(a, b):
    c = a + b
    print(f"{a} + {b} = {c}")
    return c


def sub(a, b):
    c = a - b
    print(f"{a} - {b} = {c}")
    return c


def div(a, b):
    c = a / b
    print(f"{a} / {b} = {c}")
    return c


def mul(a, b):
    c = a * b
    print(f"{a} * {b} = {c}")
    return c


def main():
    print("""
_______________________          
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|""")
    calc()


main()
