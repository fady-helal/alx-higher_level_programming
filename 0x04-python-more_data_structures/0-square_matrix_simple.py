def square_matrix_simple(matrix=[]):
    new = []
    for row in matrix:
        new_row = []
        for col in row:
            new_row.append(col ** 2)
        new.append(new_row)
    return new
