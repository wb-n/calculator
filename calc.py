num1 = float(input("First Number: "))
num2 = float(input("Second Number: "))
op = input("Enter operator: ")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("invalid operand")
