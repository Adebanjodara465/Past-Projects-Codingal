def Once(a,b):
    return a * b

def loop(a,b):
    result = 0
    for i in range(b):
        result += a
    return result


a = int(input("Enter the a value: "))
b = int(input("Enter the b value: "))


print("The multiplication of the two values is: ",Once(a, b))
print("The multiplication of a by b times is: ",Once(a, b))
