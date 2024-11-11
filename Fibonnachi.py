n = int(input("Enter your number: "))  
 

def fibona(n):
    if n == 0:
       return 0
    elif n == 1:
      return 1
    else:
     result = fibona(n-1) + fibona(n-2)
     print(f"Fibona {n} = {result}")
    return result

print(f"The Fibonacci value at position {n} is: {fibona(n)}") 