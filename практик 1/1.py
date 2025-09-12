number_one = int(input("Введите первое число: "))
number_two = int(input("Введите второе число: "))
number_three = int(input("Введите третье число: "))
arif = str(input("Введите арифмитеческое действие: "))

sum = number_one + number_two + number_three
multiplication = number_one * number_two * number_three
if arif == '*':
    print("Произведение чисел: ", multiplication)
elif arif == '+':
    print("сумма чисел: ", sum)