# Python program to add two objects if both objects are an integer type.
def check(obj1, obj2):
    if type(obj1)==int and type(obj2)==int:
        sum = obj1+obj2
        print(sum)
    else:
        print("Nothing to do here.")
        
check(138, 34)