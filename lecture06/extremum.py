from numpy import linspace
from math import sin
# Некоторые пробные функции, проверял на них. Можно попробовать вставить свою
def Parabola(x):
    return x**2

def Line(x):
    return 2*x

def Cubic_parabola(x):
    return x**3

def Some_func(x):
    return -x**2 + 3*x + 1

def SinSin(x):
    return sin(sin(x))

# Решение. Немного перегружено, но работает. Ищем
def Extremum(func, a, b):
    valuesY = []
    valuesX = []
    for k in linspace(a,b,1000):
        valuesY.append(func(k))
        valuesX.append(k)
    ext_min=min(valuesY)
    x_min=valuesX[valuesY.index(ext_min)]
    ext_max=max(valuesY)
    x_max=valuesX[valuesY.index(ext_max)]
    if ext_max == func(b) and ext_min == func(a):
        y = None
        x = None
        typeE = None
    elif ext_max == func(a) or ext_max == func(b):
        y = round(ext_min,3)
        x = round(x_min,3)
        typeE = 'min'
    elif ext_min == func(a) or ext_min == func(b):
        y = round(ext_max,3)
        x = round(x_max,3)
        typeE = 'max'    
    return x,y,typeE

pr = Extremum(SinSin, 0, 2)
if pr[0] == None:
    print(pr[2]) #не имеем экстремумов
else:
    print(f"Имеем {pr[2]} функции примерно в точке x={pr[0]}, y={pr[1]}")
