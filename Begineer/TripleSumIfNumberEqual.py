a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a == b == c:
    print("All values are same. Triple sum is:", 3 * (a + b + c))
else:
    print("Values are not same. Sum is:", a + b + c)
