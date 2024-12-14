number = input("Введите целое число: ")
while type(number) != int:
    try:
        number = int(number)
    except ValueError:
        print("Ошибка: введено не целое число.")
        number = input("Введите целое число: ")
if number > 0:
    number += 1
else:
    number -= 2
print(number)
