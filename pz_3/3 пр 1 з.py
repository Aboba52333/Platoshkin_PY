#Дано трехзначное число. Проверить истинность высказывания: «Цифры данного
#числа образуют возрастающую или убывающую последовательность..»
number = input("Введите трехзначное число: ")
while type(number) != int:
    try:
        number = int(number)
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите трехзначное число.")
        number = input("Введите трехзначное число: ")
hundreds = number // 100
tens = (number // 10) % 10
units = number % 10
is_increasing = (hundreds < tens < units)
is_decreasing = (hundreds > tens > units)
if is_increasing:
    print("Цифры образуют возрастающую последовательность.")
elif is_decreasing:
    print("Цифры образуют убывающую последовательность.")
else:
    print("Цифры не образуют ни возрастающую, ни убывающую последовательность.")
