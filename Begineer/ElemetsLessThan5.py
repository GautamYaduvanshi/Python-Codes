a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# a) New list with elements less than 5
new_list = []
for i in a:
    if i < 5:
        new_list.append(i)

print("Elements less than 5:", new_list)

# b) One line solution
print("One line result:", [i for i in a if i < 5])

# c) User defined limit
limit = int(input("Enter a number: "))
user_list = [i for i in a if i < limit]
print("Elements less than", limit, ":", user_list)
