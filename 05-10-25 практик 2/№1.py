def multiply_list(numbers):
    result = 1
    for num in numbers:
        result = result * num
    return result

my_list = [2, 3, 4]
answer = multiply_list(my_list)
print("Список:", my_list)
print("Произведение:", answer)