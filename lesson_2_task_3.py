import math

def square(a):
    # Вычисляем площадь квадрата
    area = a**2
    # Округляем площадь квадрата вверх
    area = math.ceil(area)
    return area

print(square(5)) # Выводит 25
print(square(3.7)) # Выводит 14
print(square(2.1)) # Выводит 5
