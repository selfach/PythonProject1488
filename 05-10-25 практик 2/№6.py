def power_list(numbers, power):
    result = []
    for num in numbers:
        result.append(num ** power)
    return result

numbers = [1, 2, 3, 4]
print(power_list(numbers, 2))