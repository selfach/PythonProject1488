import random

original_list = []
for i in range(20):
    num = random.randint(-10, 10)
    original_list.append(num)

print("Начальный список:")
print(original_list)

middle = len(original_list) // 2
left_half = original_list[:middle]
right_half = original_list[middle:]

left_half.sort()

right_half.sort()
right_half.reverse()

result_list = left_half + right_half

print("\nРезультат:")
print(result_list)