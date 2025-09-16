# a = int(input("Введите номер дня недели"))
# if a == 1:
#     print("Понедельник")
# if a == 2:
#     print("Вторник")
# if a == 3:
#     print("среда")
# if a == 4:
#     print("четверг")
# if a == 5:
#     print("пятница")
# if a == 6:
#     print("суббота")
# if a == 7:
#     print("воскресенье")


# a = int(input("Введите номер месяца: "))
# if a == 1:
#     print("Январь")
# if a == 2:
#     print("Февраль")
# if a == 3:
#     print("Март")
# if a == 4:
#     print("Апрель")
# if a == 5:
#     print("Май")
# if a == 6:
#     print("Июнь")
# if a == 7:
#     print("Июль")
# if a == 8:
#     print("Август")
# if a == 9:
#     print("Сентярбрь")
# if a == 10:
#     print("Октябрь")
# if a == 11:
#     print("Ноябрь")
# if a == 12:
#     print("Декабрь")


# a = int(input("Введите число: "))
# if a>0:
#     print("number is posotive")
# elif a<0:
#     print("Number is negativ")
# elif a==0:
#     print("Number is equal of zero")
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# if a != b:
#     print(*sorted([a,b]))
# user_number = int(input())
# if 1 <= user_number <= 100:
#     if user_number % 5 == 0 and
#      user_number % 3 == 0:
#      print("FIZ BUZ")
#     elif user_number % 3 == 0:
#         print("FIZ")
#     elif user_number % 5 == 0:
#        print("BUZ")
#     else:
#         print(user_number)
# else:
#     print("Неверно")


# lists = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
# number = int(input("Введите число: ")) - 1
# print(lists[number])
# number = int(input("Введите число от 1 до 7:  "))
# if number == 1:
#     print("Понедельник")
# elif number == 2:
#         print("вт")
# elif number == 7:
#     print("вс")
# elif number == 3:
#     print("ср")
# elif number == 4:
#     print("чт")
# elif number == 5:
#     print("пт")
# elif number == 6:
#     print("сб")
# elif number == 7:
#     print("вс")
# else:
#     print("вы ввели неправильно число")
#

#выполнение внутреннего кода
# for i in range(1,100):
#     print("апаю ммр день", i)
#while (условие)
# while True:
#     print("----")
# value_user = 1
# sum_user = 1000
# while value_user != 0: #пока выполняется условие
#     value_user = int(input("число для сумирования: "))
#     sum_user = sum_user - value_user
# print("Сумма чисел:", sum_user)
#*
#**
#***
#****
#*****
#******
# print("*\n**\n***\n****\n*****")
# lol = 5
# i = 1
# while i <= lol:
#     print('*' * i)
#     i+=1
#
#Пользователь вводит строку
#необходимо проверить ее на палиндром
#кок, а буду я у дуба,
user_string = input("Введите строку для проверки на Палиндром: ")
cunter_letter = len(user_string) #функция подсчета
value_user = True #перменная для проверки палиндрома
#кол-ва элимента
for letter_begin in range(0, counter_letter):
    for letter_end in range(counter_letter, 0, -1):
        print("Проверяется буква:",user_string[letter_begin])
        print("Проверяется буква:",user_string[letter_end])
        if letter_begin != letter_end:
            value_user = False
            break
    if value_user == False:
        print("слово не является палиндромом")
        break
