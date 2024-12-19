#Даны целые положительные числа N и K. Найти сумму 1K + 2К + ... + NK. 
N = input("Введите целое положительное число N: ")
K = input("Введите целое положительное число K: ")

while True:
    try:
        N = int(N)
        K = int(K)
        if N > 0 and K > 0:
            break
        else:
            print("Ошибка: N и K должны быть положительными целыми числами.")
            N = input("Введите целое положительное число N: ")
            K = input("Введите целое положительное число K: ")
    except ValueError:
        print("Неправильно ввели! Введите положительные целые числа.")
        N = input("Введите целое положительное число N: ")
        K = input("Введите целое положительное число K: ")

# Вычисление суммы
total_sum = 0
for i in range(1, N + 1):
    total_sum += i ** K

print("Сумма 1K + 2K + ... + NK =", total_sum)
