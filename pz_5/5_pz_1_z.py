#С помощью функций получить вертикальную и горизонтальную линии. Линия
#проводится многократной печатью символа. Заключить слово в рамку из
#полученных линий.

def horizontal_line(length):
    """Функция для создания горизонтальной линии."""
    print('*' * length)

def vertical_line(length):
    """Функция для создания вертикальной линии."""
    for _ in range(length):
        print('*')

def print_frame(word):
    """Функция для заключения слова в рамку."""
    length = len(word) + 2  
    horizontal_line(length)
    print('*' + word + '*')
    horizontal_line(length)


while True:
    try:
        word = input("Введите слово: ").strip()  
        if not word:  
            raise ValueError("Слово не должно быть пустым.")
        break  
    except ValueError as e:
        print("Ошибка:", e)

print_frame(word)