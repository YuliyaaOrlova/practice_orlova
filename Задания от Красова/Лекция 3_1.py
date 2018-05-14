import random
import copy

#Функция генерирования случайной матрицы с заданным размером
def genenerate_matrix(n):
    matrix = [[str(random.randrange(10)) for i in range(n)] for j in range(n)]
    return matrix

#Функция вычисления определетиля матрицы
def determinant(matrix):
    result = 0
    length = len(matrix)
    if length == 1:
        return matrix[0][0]
    if length == 2:
        return int(matrix[0][0]) * int(matrix[1][1]) - \
               int(matrix[0][1]) * int(matrix[1][0])
    for i in range(length):
        buf_matrix = copy.deepcopy(matrix)
        for j in range(length):
            del buf_matrix[j][i]
        result += int(matrix[0][i]) * pow((-1), i) * determinant(buf_matrix[1:])
    return result

#Функция, которая осуществляет вращение матрицы на 90 градусов (True) и -90 градусов (False)
def turn_matrix(matrix, direction):
    if direction:
        buf_matrix = copy.deepcopy(matrix)
        length = len(matrix)
        for i in range(length):
            for j in range(length):
                buf_matrix[i][j] = matrix[j][length - i - 1]
    else:
        buf_matrix = copy.deepcopy(matrix)
        length = len(matrix)
        for i in range(length):
            for j in range(length):
                buf_matrix[i][j] = matrix[length - j - 1][i]
    return buf_matrix

#Функция сортировки строк или столбцов матрицы по возрастанию (True) и по убыванию (False)
def sort_matrix(matrix, sort_by, order):
    status = True
    length = len(matrix)
    buff_matrix = copy.deepcopy(matrix)
    if sort_by == 'column':
        if order:
            for k in range(length):
                for i in range(length - 1):
                    for j in range(length - i - 1):
                        if int(buff_matrix[j][k]) > int(buff_matrix[j + 1][k]):
                            buff = buff_matrix[j][k]
                            buff_matrix[j][k] = buff_matrix[j + 1][k]
                            buff_matrix[j + 1][k] = buff
                            status = False
                    if status:
                        break
        else:
            for k in range(length):
                for i in range(length - 1):
                    for j in range(length - i - 1):
                        if int(buff_matrix[j][k]) < int(buff_matrix[j + 1][k]):
                            buff = buff_matrix[j][k]
                            buff_matrix[j][k] = buff_matrix[j + 1][k]
                            buff_matrix[j + 1][k] = buff
                            status = False
                    if status:
                        break
    elif sort_by == 'row':
        if order:
            for k in range(length):
                for i in range(length - 1):
                    for j in range(length - i - 1):
                        if int(buff_matrix[k][j]) > int(buff_matrix[k][j + 1]):
                            buff = buff_matrix[k][j]
                            buff_matrix[k][j] = buff_matrix[k][j + 1]
                            buff_matrix[k][j + 1] = buff
                            status = False
                    if status:
                        break
        else:
            for k in range(length):
                for i in range(length - 1):
                    for j in range(length - i - 1):
                        if int(buff_matrix[k][j]) < int(buff_matrix[k][j + 1]):
                            buff = buff_matrix[k][j]
                            buff_matrix[k][j] = buff_matrix[k][j + 1]
                            buff_matrix[k][j + 1] = buff
                            status = False
                    if status:
                        break
    else:
        print('Некорректное значение sort_by!')
    return buff_matrix

#Функция сортирует все элементы матрицы по возрастанию (True) или по убыванию (False)
def sort_matrix_by_all(matrix, order):
    buf_matrix = []
    copy_matrix = copy.deepcopy(matrix)
    length = len(matrix)
    flag = True
    for i in range(length):
        for j in range(length):
            buf_matrix.append(matrix[i][j])
    length_buff = len(buf_matrix)
    if order:
        for i in range(length_buff - 1):
            for j in range(length_buff - i - 1):
                if int(buf_matrix[j]) < int(buf_matrix[j + 1]):
                    buff = buf_matrix[j]
                    buf_matrix[j] = buf_matrix[j + 1]
                    buf_matrix[j + 1] = buff
                    flag = False
            if flag:
                break
    else:
        for i in range(length_buff - 1):
            for j in range(length_buff - i - 1):
                if int(buf_matrix[j]) > int(buf_matrix[j + 1]):
                    buff = buf_matrix[j]
                    buf_matrix[j] = buf_matrix[j + 1]
                    buf_matrix[j + 1] = buff
                    flag = False
            if flag:
                break
    for i in range(length):
        for j in range(length):
            copy_matrix[i][j] = buf_matrix[i * length + j]
    return copy_matrix

#Функция, возвращающая преобразованную матрицы с изменеными позициями наибольших и наименьших значений
def swap_min_max(matrix):
    status = True
    copy_matrix = copy.deepcopy(matrix)
    for i in range(len(matrix[0])):
        for j in range(len(matrix[0])):
            if status:
                minimum = int(matrix[i][j])
                i_min = i
                j_min = j
                maximum = int(matrix[i][j])
                i_max = i
                j_max = j
                status = False
            else:
                if int(matrix[i][j]) > maximum:
                    maximum = int(matrix[i][j])
                    i_max = i
                    j_max = j
                if int(matrix[i][j]) < minimum:
                    minimum = int(matrix[i][j])
                    i_min = i
                    j_min = j
    buff = copy_matrix[i_min][j_min]
    copy_matrix[i_min][j_min] = copy_matrix[i_max][j_max]
    copy_matrix[i_max][j_max] = buff
    print('Минимальный элемент с индексами [%s][%s]: %s' % (i_min, j_min, minimum))
    print('Максимальный элемент с индексами [%s][%s]: %s' % (i_max, j_max, maximum))
    return copy_matrix

#Ф-ция возвращает преобразовнную матрицу matrix, сортируя столбцы
def sort_by_summ(matrix, sort_by, order):
    length = len(matrix)
    status = True
    array_of_summ = [[i, 0] for i in range(length)]
    buff_matrix = [[0 for i in range(length)] for j in range(length)]
    if sort_by == 'column':
        if order:
            for i in range(length):
                for j in range(length):
                    array_of_summ[i][1] += int(matrix[j][i])
            for i in range(length - 1):
                for j in range(length - i - 1):
                    if array_of_summ[j][1] > array_of_summ[j + 1][1]:
                        buff_0 = array_of_summ[j + 1][0]
                        buff_1 = array_of_summ[j + 1][1]
                        array_of_summ[j + 1][0] = array_of_summ[j][0]
                        array_of_summ[j + 1][1] = array_of_summ[j][1]
                        array_of_summ[j][0] = buff_0
                        array_of_summ[j][1] = buff_1
                        status = False
                if status:
                    break
            for i in range(length):
                if i != array_of_summ[i][0]:
                    for j in range(length):
                        buff_matrix[j][i] = matrix[j][array_of_summ[i][0]]
                else:
                    for j in range(length):
                        buff_matrix[j][i] = matrix[j][i]
        else:
            for i in range(length):
                for j in range(length):
                    array_of_summ[i][1] += int(matrix[j][i])
            for i in range(length - 1):
                for j in range(length - i - 1):
                    if array_of_summ[j][1] < array_of_summ[j + 1][1]:
                        buff_0 = array_of_summ[j + 1][0]
                        buff_1 = array_of_summ[j + 1][1]
                        array_of_summ[j + 1][0] = array_of_summ[j][0]
                        array_of_summ[j + 1][1] = array_of_summ[j][1]
                        array_of_summ[j][0] = buff_0
                        array_of_summ[j][1] = buff_1
                        status = False
                if status:
                    break
            for i in range(length):
                if i != array_of_summ[i][0]:
                    for j in range(length):
                        buff_matrix[j][i] = matrix[j][array_of_summ[i][0]]
                else:
                    for j in range(length):
                        buff_matrix[j][i] = matrix[j][i]
    elif sort_by == 'row':
        if order:
            for i in range(length):
                for j in range(length):
                    array_of_summ[i][1] += int(matrix[i][j])
            for i in range(length - 1):
                for j in range(length - i - 1):
                    if array_of_summ[j][1] > array_of_summ[j + 1][1]:
                        buff_0 = array_of_summ[j + 1][0]
                        buff_1 = array_of_summ[j + 1][1]
                        array_of_summ[j + 1][0] = array_of_summ[j][0]
                        array_of_summ[j + 1][1] = array_of_summ[j][1]
                        array_of_summ[j][0] = buff_0
                        array_of_summ[j][1] = buff_1
                        status = False
                if status:
                    break
            for i in range(length):
                if i != array_of_summ[i][0]:
                    for j in range(length):
                        buff_matrix[i][j] = matrix[array_of_summ[i][0]][j]
                else:
                    for j in range(length):
                        buff_matrix[i][j] = matrix[i][j]
        else:
            for i in range(length):
                for j in range(length):
                    array_of_summ[i][1] += int(matrix[i][j])
            for i in range(length - 1):
                for j in range(length - i - 1):
                    if array_of_summ[j][1] < array_of_summ[j + 1][1]:
                        buff_0 = array_of_summ[j + 1][0]
                        buff_1 = array_of_summ[j + 1][1]
                        array_of_summ[j + 1][0] = array_of_summ[j][0]
                        array_of_summ[j + 1][1] = array_of_summ[j][1]
                        array_of_summ[j][0] = buff_0
                        array_of_summ[j][1] = buff_1
                        status = False
                if status:
                    break
            for i in range(length):
                if i != array_of_summ[i][0]:
                    for j in range(length):
                        buff_matrix[i][j] = matrix[array_of_summ[i][0]][j]
                else:
                    for j in range(length):
                        buff_matrix[i][j] = matrix[i][j]
    else:
        print('Некорректное значение sort_by!')
    return buff_matrix

#Функция возведения матрицы в степень
def exponentiation_matrix(matrix, degree):
    length = len(matrix)
    copy_matrix = [[0 for i in range(length)] for j in range(length)]
    buff_matrix = copy.deepcopy(matrix)
    if degree == 0:
        return [['1', '0', '0'], ['0', '1', '0'], ['0', '0', '1']]
    elif degree == 1:
        return buff_matrix
    else:
        for st in range(degree - 1):
            for i in range(length):
                for j in range(length):
                    for k in range(length):
                        copy_matrix[i][j] += int(matrix[i][k]) * \
                                             int(buff_matrix[k][j])
            buff_matrix = copy.deepcopy(copy_matrix)
            copy_matrix = [[0 for i in range(length)] for j in range(length)]
        for i in range(length):
            for j in range(length):
                buff_matrix[i][j] = str(buff_matrix[i][j])
        return buff_matrix

#Функция, транспонирующая матрицу
def transpose(matrix):
    buff_matrix = copy.deepcopy(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            buff_matrix[i][j] = matrix[j][i]
    return buff_matrix

#Функция возвращает минор
def minor(matrix, i, j):
    buff_matrix = copy.deepcopy(matrix)
    del buff_matrix[i]
    for k in range(len(buff_matrix)):
        del buff_matrix[k][j]
    return buff_matrix

#Функция возвращает обратную матрицу
def inverse_matrix(matrix):
    det = determinant(matrix)
    if det == 0:
        print('У данной матрицы не существует обратной матрицы!\n')
        return ''
    length = len(matrix)
    buff_matrix = copy.deepcopy(matrix)
    buff_matrix = transpose(buff_matrix)
    matrix_of_alg_compl = [['0' for i in range(length)]
                           for j in range(length)]
    for i in range(length):
        for j in range(length):
            matrix_of_alg_compl[i][j] = pow(-1, (i + j + 2)) * \
                                        determinant(minor(buff_matrix, i, j))
    for i in range(length):
        for j in range(length):
            if matrix_of_alg_compl[i][j] == 0:
                buff_matrix[i][j] = '0'
            else:
                buff_matrix[i][j] = str(matrix_of_alg_compl[i][j] / det)
    return buff_matrix

#Функция, которая выводит все элементы матрицы
def print_matrix(matrix):
    for row in matrix:
        print(' '.join(row))
    print('\n')


def main():
    n = int(input('Введите размер квадратной матрицы: '))
    matrix = genenerate_matrix(n)
    print('Сгенерированная матрица ', n, 'x', n, ':\n')
    print_matrix(matrix)
    print('Определитель матрицы: ', determinant(matrix), '\n')
    print('Матрица повернутая на 90 град. против часовой стрелке:\n')
    print_matrix(turn_matrix(matrix, direction=True))
    print('Та же матрица повернутая на 90 град. по часовой стрелке:\n')
    print_matrix(turn_matrix(matrix, direction=False))
    print('Матрица, в которой столбцы отсортированы по убыванию:\n')
    print_matrix(sort_matrix(matrix, 'column', False))
    print('Матрица, в которой столбцы отсортированы по возрастанию:\n')
    print_matrix(sort_matrix(matrix, 'column', True))
    print('Матрица, в которой строки отсортированы по убыванию:\n')
    print_matrix(sort_matrix(matrix, 'row', False))
    print('Матрица, в которой строки отсортированы по возрастанию:\n')
    print_matrix(sort_matrix(matrix, 'row', True))
    print('Матрица, отсортированная по элементам по убыванию:\n')
    print_matrix(sort_matrix_by_all(matrix, True))
    print('Матрица, отсортированная по элементам по возрастанию:\n')
    print_matrix(sort_matrix_by_all(matrix, False))
    print('Матрица, в которой минимальный и максимальный\n',
          'элементы поменяли местами:\n')
    print_matrix(swap_min_max(matrix))
    print('Матрица, в которой столбцы отсортированны по убыванию\n',
          'суммы элементов в них:\n')
    print_matrix(sort_by_summ(matrix, 'column', False))
    print('Матрица, в которой столбцы отсортированны по возрастанию\n'
          'суммы элементов в них:\n')
    print_matrix(sort_by_summ(matrix, 'column', True))
    print('Матрица, в которой строки отсортированны по убыванию\n',
          'суммы элементов в них:\n')
    print_matrix(sort_by_summ(matrix, 'row', False))
    print('Матрица, в которой строки отсортированны по возрастанию\n',
          'суммы элементов в них:\n')
    print_matrix(sort_by_summ(matrix, 'row', True))
    print('Матрица в степени 2:\n')
    print_matrix(exponentiation_matrix(matrix, 2))
    print('Матрица в степени 3:\n')
    print_matrix(exponentiation_matrix(matrix, 3))
    print('Матрица в степени 4:\n')
    print_matrix(exponentiation_matrix(matrix, 4))
    print('Матрица обратная данной: \n')
    print_matrix(inverse_matrix(matrix))


if __name__ == '__main__':
    main()