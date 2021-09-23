# Finding GCD aka HCF of two positive integers.
n1 = int(input("Enter the first number:"))
n2 = int(input("Enter the second number:"))

#Finding lcm
def lcm():
    global maxNum
    maxNum = max(n1,n2)
    while True:
        if (maxNum%n1==0) and (maxNum%n2==0):
            break
        maxNum+=1

def gcd():
    lcm()
    Gcd = n1*n2/maxNum
    return Gcd

print(gcd())