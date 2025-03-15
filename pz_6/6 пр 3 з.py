#Дано множество A из N точек (точки заданы своими координатами x, у). Среди всех
#точек этого множества, лежащих в первой или третьей четверти, найти точку,
#наиболее близкую к началу координат. Если таких точек нет, то вывести точку с
#нулевыми координатами.
#Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется по формуле:
#R = √(x2 – x1)2 + (у2 – y1)2
#Для хранения данных о каждом наборе точек следует использовать по два списка: первый
#список для хранения абсцисс, второй — для хранения ординат.

import math

def closest_point(points_x, points_y):
    closest_distance = float('inf')
    closest_index = -1

    for i in range(len(points_x)):
        if (points_x[i] > 0 and points_y[i] > 0) or (points_x[i] < 0 and points_y[i] < 0):
            distance = math.sqrt(points_x[i] ** 2 + points_y[i] ** 2)
            if distance < closest_distance:
                closest_distance = distance
                closest_index = i

    if closest_index == -1:
        return (0, 0)  
    else:
        return (points_x[closest_index], points_y[closest_index])

while True:
    try:
        N = int(input("Введите количество точек: "))
        if N <= 0:
            raise ValueError("Количество точек должно быть положительным.")
        
        points_x = []
        points_y = []

        for i in range(N):
            x = float(input(f"Введите x для точки {i + 1}: "))
            y = float(input(f"Введите y для точки {i + 1}: "))
            points_x.append(x)
            points_y.append(y)

        closest = closest_point(points_x, points_y)
        print("Ближайшая точка к началу координат:", closest)
        break
    except ValueError as e:
        print("Ошибка:", e)
