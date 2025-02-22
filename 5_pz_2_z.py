import math

def TrianglePS(a):
    """Вычисляет периметр и площадь равностороннего треугольника по стороне a."""
    P = 3 * a  # Периметр
    S = (a ** 2 * math.sqrt(3)) / 4  # Площадь
    return P, S  # Возвращаем периметр и площадь

# Ввод сторон треугольников от пользователя
triangles = []
for i in range(3):
    while True:
        try:
            a = float(input(f"Введите длину стороны равностороннего треугольника {i + 1}: "))
            if a <= 0:  # Проверка на положительность
                raise ValueError("Длина стороны должна быть положительной.")
            triangles.append(a)
            break  # Выход из цикла, если ввод корректен
        except ValueError as e:
            print("Ошибка:", e)

# Вычисление и вывод периметров и площадей для введенных сторон
for i, a in enumerate(triangles, start=1):
    try:
        P, S = TrianglePS(a)
        print(f"Треугольник {i}: Периметр = {P:.2f}, Площадь = {S:.2f}")
    except Exception as e:
        print("Произошла ошибка при вычислении:", e)