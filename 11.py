import math
sides=(input('Введите велечины сторон треугольника: '))
sides=sides.split(' ')
a=float(sides[0])
b=float(sides[1])
c=float(sides[2])
angle_a = math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c)))
angle_b = math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c)))
angle_c = 180 - angle_a - angle_b
print(angle_a, angle_b, angle_c)