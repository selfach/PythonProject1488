backpack = {"Зажигалка":20, "Компас":100, "Фрукты":500, "Рубашка":300,
           "Термос":1000, "Аптечка":200, "Куртка":600, "Бинокль":400,
           "Удочка":1300, "Салфетки":40, "Бутерброды":800, "Палатка":5500,
           "Спальный мешок":2500, "Изолента":250, "Котел":3000}

massa = int(input("Введите допустимый вес рюкзака (в кг): ")) * 1000

can_take = {k:v for k,v in backpack.items() if v <= massa}
cannot_take = {k:v for k,v in backpack.items() if v > massa}

print(f"\nМогу взять (всего {sum(can_take.values())}г):")
for key, value in can_take.items():
    print(f"{key}: {value}г")

print(f"\nНе могу взять (слишком тяжелые):")
for key, value in cannot_take.items():
    print(f"{key}: {value}г")