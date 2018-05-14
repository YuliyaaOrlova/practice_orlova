print ("Введите коэффициенты квадратного уравнения: ")
a = int (input("a = "))
b = int (input("b = "))
c = int (input("c = "))

D = b**2 - 4*a*c
print ("\nДискриминант D = %.3f" % D)
if D > 0:
    import math
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print("x1 = %.3f \nx2 = %.3f" % (x1, x2))
elif D == 0:
    x = -b / (2 * a)
    print("x = %.3f" % x)
else:
    print("Корней нет")
