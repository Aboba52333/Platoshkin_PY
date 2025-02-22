def transform_list(A):
    B = []
    for AK in A:
        if AK < 5:
            B.append(2 * AK)
        else:
            B.append(AK / 2)
    return B


# Пример использования
while True:
    try:
        N = int(input("Введите размер списка: "))
        if N <= 0:
            raise ValueError("Размер списка должен быть положительным.")
        A = [int(input(f"Введите элемент {i + 1}: ")) for i in range(N)]
        B = transform_list(A)
        print("Новый список B:", B)
        break
    except ValueError as e:
        print("Ошибка:", e)