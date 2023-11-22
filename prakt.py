def generate_stairs():
    with open('output.txt', 'w') as file:
        for i in range(1, 11):  # Генерируем лесенку от 1 до 10 ступенек
            stair = '*' * i  # Создаем строку с символами '*' для текущей ступеньки
            file.write(stair + '\n')  # Записываем строку в файл с добавлением символа переноса строки

generate_stairs()