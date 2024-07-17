
def cal_1():
    num1 = float(input("Enter the first number: "))
    op = input("Enter the operator. EX: + - / * : ")
    num2 = float(input("Enter the second number: "))

    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "/":
        print(num1 / num2)
    elif op == "*":
        print(num1 * num2)
    else:
        print("Invalid operator")
