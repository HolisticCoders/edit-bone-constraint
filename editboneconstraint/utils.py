from math import isclose


def flatten_matrix(matrix):
    dim = len(matrix)
    return [matrix[j][i] for i in range(dim) for j in range(dim)]


def lerp(a, b, factor):
    return a + factor * (b - a)


def matrices_are_equal(mat1, mat2):
    for row1, row2 in zip(mat1, mat2):
        for float1, float2 in zip(row1, row2):
            if not isclose(
                float1, float2, abs_tol=0.001
            ):  # NOTE: 0.001 might not be the best value here
                return False
    return True
