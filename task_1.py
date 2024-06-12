# Напишите функцию для транспонирования матрицы

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def trans_1(data):
    trans_matrix = [[data[i][j] for i in range(len(data))] for j in range(len(data[0]))]
    return trans_matrix


def trans_2(data):
    trans_matrix = [[], [], []]
    for i in range(len(data)):
        for j in range(len(data[0])):
            trans_matrix[i].append(data[j][i])
    return trans_matrix


print(f'{matrix = }\n{trans_1(matrix) = }\n{trans_2(matrix) = }')

