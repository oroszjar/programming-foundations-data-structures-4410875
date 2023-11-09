def find_second_smallest(my_list):
    for item in my_list:
        if not type(item)==int:
            return None
    if not my_list:
        return None
    elif len(my_list)==1:
        return None
    else:
        return sorted(my_list)[1]


print(find_second_smallest([]))
print(find_second_smallest([1]))
print(find_second_smallest(['asd', 1, 2, 3]))
print(find_second_smallest([1.2, 2, 3]))
print(find_second_smallest([5, 8, 3, 2, 6]))
print(find_second_smallest([1,2,3,4,5,6]))

# find second smallest item in list of ints
# list can have any number of items
# list has no duplicates