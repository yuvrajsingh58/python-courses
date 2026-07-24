num1 = int(input("Enter the first number: "))

num2 = int(input("Enter the second number: "))

print("Addition", num1 + num2)
print("Subtraction", num1 - num2)
print("Multiplacation", num1 * num2)
# print("Division", num1 / num2)
if num2 != 0:
    print("Division =", num1 / num2)
    print("Floor Division =", num1 // num2)
    print("Modulus =", num1 % num2)
    print("Division =", num1 / num2)
else:
    print("Division by zero is not allowed.")

