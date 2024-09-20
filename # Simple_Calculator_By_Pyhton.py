# Simple_Calculator_By_Pyhton

operator = input("Enter an Operatot (+ - * /): ")
num1 = float(input("Enter 1st Number: "))
num2 = float(input("Enter 2nd Number: "))

if operator == "+":
    result = (num1 + num2)
    print(round(result, 2))
elif operator == "-":
    result = (num1 - num2)
    print(round(result, 2))
elif operator == "*":
    result = (num1 * num2)
    print(round(result, 2))
elif operator == "/":
    result = (num1 / num2)
    print(round(result, 2))

else:
    print(f"{operator} is Invalid")
