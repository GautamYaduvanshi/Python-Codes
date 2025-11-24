def is_present(lst, num):
    if num in lst:
        return True
    else:
        return False

numbers = [1, 3, 5, 7, 9, 11, 13]

value = int(input("Enter number to search: "))

print(is_present(numbers, value))
