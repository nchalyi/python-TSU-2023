from math import sqrt, cos
b = float(input("Введите длину первой стороны >> "))
c = float(input("Введите длину второй стороны >> "))
angl = float(input("Введите угол между сторонами (в радианах) >> "))
print("Длина третьей стороны >> ", sqrt (b**2 + c**2 - 2*b*c*cos(angl)))
input()
