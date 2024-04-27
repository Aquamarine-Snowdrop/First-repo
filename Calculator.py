def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multiply(a,b):
    return a*b

def div(a,b):
    return a/b

op = input("Enter operator (/ , * , + , - ) = ")
num1 = int(input("Enter first number = "))
num2 = int(input("Enter second number = "))

if op == '+':
    print("Sum = ", str(add(num1 , num2)))
elif op == '-':
    print("Difference = ", str(sub(num1 , num2)))
elif op == '*':
    print("Product = ", str(multiply(num1 , num2)))
elif op == '/':
    print("Sum = ", str(add(num1 , num2)))
else:
    print("Operator invalid")
    


