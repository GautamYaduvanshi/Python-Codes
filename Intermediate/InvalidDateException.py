from datetime import datetime

try:
    name = input("Enter your name: ")
    dob = input("Enter your Date of Birth (DD-MM-YYYY): ")

    datetime.strptime(dob, "%d-%m-%Y")   # date validation

    print("Name:", name)
    print("Date of Birth:", dob)

except:
    print("Invalid Date Entered!")
