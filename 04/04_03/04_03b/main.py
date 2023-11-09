set_A = {10, 20, 30, 40, 50}
set_B = {30, 40, 50, 60, 70}

union_set = set_A.union(set_B)
print(union_set)

intersection_set = set_A.intersection(set_B)
print(intersection_set)

difference_setAB = set_A.difference(set_B)
print(difference_setAB)
difference_setBA = set_B.difference(set_A)
print(difference_setBA)

symmetric_difference_set = set_A.symmetric_difference(set_B)
print(symmetric_difference_set)