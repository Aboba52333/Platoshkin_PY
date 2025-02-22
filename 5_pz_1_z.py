def horizontal_line(length):
    """Функция для создания горизонтальной линии."""
    print('*' * length)

def vertical_line(length):
    """Функция для создания вертикальной линии."""
    for _ in range(length):
        print('*')

def print_frame(word):
    """Функция для заключения слова в рамку."""
    length = len(word) + 2  # Длина рамки равна длине слова + 2 для границ
    horizontal_line(length)
    print('*' + word + '*')
    horizontal_line(length)

# Ввод слова с обработкой исключений
while True:
    try:
        word = input("Введите слово: ").strip()  # Убираем пробелы в начале и в конце
        if not word:  # Проверка на пустую строку
            raise ValueError("Слово не должно быть пустым.")
        break  # Выход из цикла, если ввод корректен
    except ValueError as e:
        print("Ошибка:", e)

# Вывод рамки с введенным словом
print_frame(word)