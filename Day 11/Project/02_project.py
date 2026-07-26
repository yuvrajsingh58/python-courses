try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Addition =", num1 + num2)
    print("Subtraction =", num1 - num2)
    print("Multiplication =", num1 * num2)
    print("Division =", num1 / num2)

except ZeroDivisionError:
    print("Division by zero not allowed.")

except ValueError:
    print("Please enter a valid number.")

else:
    print("All calculations completed successfully.")

finally:
    print("Thank you for using Safe Calculator!")