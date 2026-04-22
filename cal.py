choice=input("enter your choice:")
num1=int(input("enter your first number:"))
num2=int(input("enter your second number:"))
print("select operation")
print("1. Add")
print("2. Subtract")
print("3. Multiplication")
if choice=='1':
    print(num1+num2)
elif choice=='2':
    print(num1-num2)
else:
    print(num1*num2)
