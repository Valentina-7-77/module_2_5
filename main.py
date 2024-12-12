    # Матрица воплоти

                                            # Объявляем функцию с тремя параметрами
def get_matrix(n, m, value):
    matrix = []                             # Создаем пустой список
    for i in range (0, n):                  # Внешний цикл, количество строк
        matrix1 = []                        # Пустой список (пустая строка)
        for j in range (0, m):              # Внутренний цикл, добавляем значение в строку
            matrix1.append (value)
        matrix.append (matrix1)
    return matrix                           # Возвращаем матрицу
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
                                            # Выводим результаты
print(result1)
print(result2)
print(result3)