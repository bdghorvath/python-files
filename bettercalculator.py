
num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))
op = input("Enter in an operator: ")

while op != ("+" or "-" or "*" or "/" or "%%"):
    op = input("Enter in an operator: ")

if op == "+":
    print(num1 + num2)
    
elif op == "-":
    print(num1 - num2)
    

elif op == "*":
    print(num1 * num2)

elif op == "/":
    print(num1 / num2)
    
elif op == "%":
    print(num1 % num2)
    