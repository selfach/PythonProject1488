# Задание 1
def bill_gates_quote():
    print("\n\"Don't compare yourself with anyone in this world…if you do so, you are insulting yourself.\"")
    print("Bill Gates")


# Задание 2
def even_numbers():
    print("\n--- Четные числа в диапазоне ---")
    try:
        start = int(input("Введите первое число: "))
        end = int(input("Введите второе число: "))

        if start > end:
            start, end = end, start

        print(f"Четные числа между {start} и {end}:")
        found = False
        for num in range(start + 1, end):
            if num % 2 == 0:
                print(num, end=" ")
                found = True
        if not found:
            print("четных чисел нет")
        print()
    except ValueError:
        print("Ошибка: введите целые числа!")


# Задание 3
def draw_square():
    print("\n--- Рисование квадрата ---")
    try:
        size = int(input("Введите длину стороны квадрата: "))
        symbol = input("Введите символ: ")[0]  # берем первый символ
        filled = input("Заполненный квадрат? (да/нет): ").lower() == 'да'

        for i in range(size):
            for j in range(size):
                if filled or i == 0 or i == size - 1 or j == 0 or j == size - 1:
                    print(symbol, end=" ")
                else:
                    print(" ", end=" ")
            print()
    except (ValueError, IndexError):
        print("Ошибка ввода данных!")


# меню
def main_menu():
    while True:
        print("\n" + "=" * 40)
        print("           ГЛАВНОЕ МЕНЮ")
        print("=" * 40)
        print("1 - Цитата Билла Гейтса")
        print("2 - Четные числа в диапазоне")
        print("3 - Нарисовать квадрат")
        print("0 - Выход")
        print("=" * 40)

        choice = input("Выберите задание (0-3): ")

        if choice == '1':
            bill_gates_quote()
        elif choice == '2':
            even_numbers()
        elif choice == '3':
            draw_square()
        elif choice == '0':
            print("До свидания!")
            break
        else:
            print("Неверный выбор! Попробуйте снова.")


# Запуск программы
if __name__ == "__main__":
    main_menu()