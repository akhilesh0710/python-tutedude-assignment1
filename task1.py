num1 = float(input("enter the first number :"))
num2 = float(input("enter the second number :"))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

if num2 != 0:
    division = num1/num2
else:
    division = "Undefined (cannot divide by zero)"

print(f"Addition : {addition}")
print(f"Subtraction : {subtraction}")
print(f"Multiplication : {multiplication}")
print(f"Division : {division}")