from math import sqrt, cos
b = float(input("Введите первую сторону >> "))
c = float(input("Введите вторую сторону >> "))
angl = float(input("Введите угол между сторонами (в радианах)>> "))
### Вопрос: а можно ли сделать так, чтобы пользователь просто вводил градусы?
print("Длина третьей стороны >> ", sqrt (b**2 + c**2 - 2*b*c*cos(angl)))
input()
