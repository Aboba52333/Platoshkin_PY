def is_arithmetic_progression(arr):
    if len(arr) < 2:
        return 0  # Для списка с менее чем двумя элементами не может быть прогрессии

    arr.sort()  # Сортируем массив для проверки прогрессии
    diff = arr[1] - arr[0]  # Разность между первым и вторым элементами

    for i in range(2, len(arr)):
        if arr[i] - arr[i - 1] != diff:
            return 0  # Если разность не совпадает, то это не прогрессия

    return diff  # Возвращаем разность прогрессии


# Пример использования
while True:
    try:
        N = int(input("Введите размер списка: "))
        if N < 2:
            raise ValueError("Размер списка должен быть не менее 2.")
        arr = [int(input(f"Введите элемент {i + 1}: ")) for i in range(N)]
        result = is_arithmetic_progression(arr)
        print("Разность прогрессии:" if result else "Не образует арифметическую прогрессию.", result)
        break
    except ValueError as e:
        print("Ошибка:", e)