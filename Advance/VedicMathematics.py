def multiply_11(n):
    s = str(n)
    result = s[0]
    
    for i in range(len(s)-1):
        result += str(int(s[i]) + int(s[i+1]))
    
    result += s[-1]
    return result

def square_5(n):
    first = n // 10
    return str(first * (first + 1)) + "25"

choice = int(input("1. Multiply by 11\n2. Square a number ending with 5\nEnter choice: "))

if choice == 1:
    num = int(input("Enter number: "))
    print("Result:", multiply_11(num))

elif choice == 2:
    num = int(input("Enter number (ending in 5): "))
    if num % 10 == 5:
        print("Result:", square_5(num))
    else:
        print("Number must end with 5!")
