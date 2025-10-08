def remove_number(numbers, target):
    count = 0
    i = 0
    while i < len(numbers):
        if numbers[i] == target:
            numbers.pop(i)
            count += 1
        else:
            i += 1
    return count

numbers = [1, 2, 3, 2, 4, 2, 5]
result = remove_number(numbers, 2)
print(result)
print(numbers)