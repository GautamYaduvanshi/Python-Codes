import re

number = input("Enter mobile number: ")

pattern = "^[7-9][0-9]{9}$"

if re.match(pattern, number):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")
