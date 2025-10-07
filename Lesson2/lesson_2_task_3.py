import math

def square(side):
    area = side * side
    return math.ceil(area)  # округляем вверх результат

# Пример вызова функции
side_length = 3.2
result = square(side_length)
print(f"Площадь квадрата со стороной {side_length}: {result}")
