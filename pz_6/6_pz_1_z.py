#Дан целочисленный список размера N, не содержащий одинаковых чисел.
#Проверить, образуют ли его элементы арифметическую прогрессию. Если образуют,
#то вывести разность прогрессии, если нет — вывести 0.

def is_arithmetic_progression(arr):
    if len(arr) < 2:
        return 0  

    arr.sort()  
    diff = arr[1] - arr[0]  

    for i in range(2, len(arr)):
        if arr[i] - arr[i - 1] != diff:
            return 0  

    return diff  


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