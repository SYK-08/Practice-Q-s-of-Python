# Finding LCM of two numbers.
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

maxNum = max(num1, num2)

while True:
    if (maxNum%num1==0 and maxNum%num2==0):
        break
    maxNum+=1

print(f"The LCM of {num1} and {num2} is: {maxNum} ")