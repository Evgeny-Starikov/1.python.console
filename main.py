# Задача 2.

length = input('Введите длину стороны квадрата: ')

perimetr = int(length) * 4
square = pow(int(length), 2)
print('Площадь квадрата равна', square, 'Периметр квадрата равен', perimetr)

print() # ввод пустой строки для разделения

length = input('Введите длину прямоугольника: ')
width = input('Введите ширину прямоугольника: ')
perimetr = (int(length) + int(width)) * 2
square = int(length) * int(width)
print('Площадь прямоугольника равна', square, 'Периметр прямоугольника равен', perimetr)

