def find_minimum(numbers):
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val

print(find_minimum([5, 2, 8, 1, 9]))