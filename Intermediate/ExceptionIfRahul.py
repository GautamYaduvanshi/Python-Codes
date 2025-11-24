try:
    name = input("Enter your name: ")

    if name.lower() == "rahul":
        raise Exception("Sorry Rahul, you are not allowed.")

    print("Hello", name)

except Exception as e:
    print(e)
