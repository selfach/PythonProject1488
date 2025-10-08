def combine_lists(list1, list2):
    result = []
    for item in list1:
        result.append(item)
    for item in list2:
        result.append(item)
    return result

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(combine_lists(list1, list2))