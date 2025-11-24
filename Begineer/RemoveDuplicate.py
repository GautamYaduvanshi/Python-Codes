def remove_duplicates(lst):
    new_list = []

    for i in lst:
        if i not in new_list:
            new_list.append(i)

    return new_list

nums = [1, 2, 2, 3, 4, 4, 5, 6, 6]
print("New list:", remove_duplicates(nums))
