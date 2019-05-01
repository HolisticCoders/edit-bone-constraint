def flatten_matrix(matrix):
    dim = len(matrix)
    return [matrix[j][i] for i in range(dim) 
                      for j in range(dim)]