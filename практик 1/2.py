number_one = int(input("Введите первое число: "))
number_two = int(input("Введите второе число: "))
number_three = int(input("Введите третье число: "))

if number_one > number_two and number_one > number_three:
    print(number_one, "макс число")
elif number_two > number_one and number_two > number_three:
    print(number_two, "макс число")
elif number_three > number_one and number_three > number_two:
    print(number_three, "макс число")
elif number_one == number_two and number_one != number_three:
    print("первое и второе число равны")
elif number_two == number_three and number_two != number_one:
    print("второе и третье число равны")
elif number_three == number_one and number_three != number_two:
    print("первое и третье число равны")
else:
    print("все числа равны")

if number_one < number_two and number_one < number_three:
    print(number_one, "мин число")
elif number_two < number_one and number_two < number_three:
    print(number_two, "мин число")
elif number_three < number_one and number_three < number_two:
    print(number_three, "мин число")
elif number_one == number_two and number_one != number_three:
    print("первое и второе число равны")
elif number_two == number_three and number_two != number_one:
    print("второе и третье число равны")
elif number_three == number_one and number_three != number_two:
    print("первое и третье число равны")
else:
    print("все числа равны")

sum = number_one + number_two + number_three
print("Средне арифметическое", sum / 3)