start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

print("1. Все числа диапазона:")
for number in range(start, end + 1):
    print(number, end=" ")
print("\n")

print("2. Все числа диапазона в убывающем порядке:")
for number in range(end, start - 1, -1):
    print(number, end=" ")
print("\n")

print("3. Все числа, кратные 7:")
count_7 = 0
for number in range(start, end + 1):
    if number % 7 == 0:
        print(number, end=" ")
        count_7 += 1
if count_7 == 0:
    print("Чисел, кратных 7, нет")
print("\n")

print("4. Количество чисел, кратных 5:")
count_5 = 0
for number in range(start, end + 1):
    if number % 5 == 0:
        count_5 += 1
print(f"Количество чисел, кратных 5: {count_5}")