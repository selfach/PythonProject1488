def rhombus_area(a, b):
    area = (a * b) / 2
    return area


a = int(input('Введите 1-ую диагональ ромба: '))
b = int(input('Введите 2-ую диагональ ромба: '))

print('Площадь ромба:', rhombus_area(a, b)) 