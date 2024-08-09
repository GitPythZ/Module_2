# Задача "Матрица воплоти":
# Напишите функцию get_matrix с тремя параметрами n, m и value, которая будет создавать матрицу(вложенный список)
# размерами n строк и m столбцов, заполненную значениями value и возвращать эту матрицу в качестве результата работы.
def get_matrix(n, m, value):
    '''Пробная докстринг - задал аргументы функции согласно задаче.'''
    matrix = []
    for _str in range(n):
        small_matrix = []
        for _columns in range(int(m)):
            small_matrix.append(value)
        matrix.append(small_matrix)
    return matrix
matrix = get_matrix(3, 3, 42)
print(f"Matrix {matrix}")
