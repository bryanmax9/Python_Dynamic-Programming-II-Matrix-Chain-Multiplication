def read_input(filename):
    # Open the specified file and read its content.
    with open(filename, 'r') as file:
        content = file.read().strip()

        # Remove the outer brackets and split the string into individual matrix dimensions.
        # This assumes the input format looks like: "{{1, 2}, {2, 3}, ...}"
        matrix_dims = content[2:-2].split("}, {")

        # Convert these dimensions to tuples of integers. This transforms strings like "1, 2"
        # into tuples like (1, 2), producing a list of matrix dimensions.
        matrix_dims = [tuple(map(int, dim.split(", "))) for dim in matrix_dims]
    return matrix_dims


def matrix_chain_order(p):
    # p contains the dimensions of the matrices such that a matrix A[i] has dimensions
    # p[i] x p[i+1]. So if there are n matrices, p has n+1 elements.

    n = len(p) - 1  # number of matrices

    # m[i][j] will hold the minimum number of scalar multiplications required to compute
    # the matrix A[i]A[i+1]...A[j].
    m = [[0 for x in range(n)] for x in range(n)]

    # s[i][j] will save the index at which to split the matrices to achieve the minimum
    # cost for multiplying matrices A[i] to A[j].
    s = [[0 for x in range(n)] for x in range(n)]

    # The algorithm considers chains of length l, starting from length 2.
    for l in range(2, n + 1):  # l is the chain length
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')

            # Try every possible split of the chain A[i]A[i+1]...A[j]
            for k in range(i, j):
                # q represents the cost of multiplying A[i]...A[k] and A[k+1]...A[j],
                # plus the cost of multiplying the two resulting matrices.
                q = m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j+1]

                # If the current split has a lesser cost than the previously recorded minimum,
                # update the minimum and save the split index.
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    # m[0][n-1] contains the minimum number of multiplications required to compute the
    # entire chain of matrices.
    return m[0][n-1]


if __name__ == "__main__":
    # Read matrix dimensions from the input file.
    matrices = read_input('10.txt')

    # Convert the list of matrix dimensions to a format suitable for the matrix chain
    # multiplication algorithm. The resulting list p contains the row size of the first matrix
    # and the column size of every matrix.
    # for example, it matrices will be "matrices = [(10, 20), (20, 30), (30, 40)]" and in the line we wil tranform to "p = [10, 20, 30, 40]"
    p = [matrices[0][0]] + [mat[1] for mat in matrices]

    # Calculate and print the minimum number of multiplications required.
    print(matrix_chain_order(p))
