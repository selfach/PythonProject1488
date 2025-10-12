import random

original_list = []
for i in range(45):
    num = random.randint(-20, 20)
    original_list.append(num)

print("Начальный список:")
print(original_list)

part_size = len(original_list) // 3
first_part = original_list[:part_size]
second_part = original_list[part_size:2*part_size]
third_part = original_list[2*part_size:]

even_nums = []
for num in first_part:
    if num % 2 == 0:
        even_nums.append(num)

max_num = max(second_part)
min_num = min(second_part)
min_max_alternate = []
for i in range(len(second_part)):
    if i % 2 == 0:
        min_max_alternate.append(max_num)
    else:
        min_max_alternate.append(min_num)

odd_nums = []
for num in third_part:
    if num % 2 != 0:
        odd_nums.append(num)

result_list = even_nums + min_max_alternate + odd_nums

print("\nРезультат:")
print(result_list)