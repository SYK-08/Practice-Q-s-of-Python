# Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20. 

n1 = int(input("Enter first number:"))
n2 = int(input("Enter second number:"))
sum = n1+n2

if sum>=15 and sum<=20:
    print(20)

else:
    print(sum) 