num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
operator = input("Enter operator: ")

if operator == "+":
    sum = num1 + num2
    print(sum)
elif operator == "-":
    difference = num1 - num2
    print(difference)
elif operator == "*":
    product = num1 * num2
    print(product)
elif operator == "/":
    quotient = num1 / num2
    print(quotient)
else:
    print("Invalid operator/input")