import math

print("Введите коэффициенты для квадратного уравнения (ax^2 + bx + c = 0):")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

d = b ** 2 - 4 * a * c
print("Дискриминант D = ", d)

if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a) #the distance that the projectile flew
    x2 = (-b - math.sqrt(d)) / (2 * a) #the point where the catapult stands
    print("the distance that the projectile flew = ", x1)
    print('the point where the catapult stands =', x2)
elif d == 0:
    x = -b / (2 * a)
    print('the point where the catapult stands = ', x)
    print('the distance that the projectile flew', x)
else:
    print("Корней нет")