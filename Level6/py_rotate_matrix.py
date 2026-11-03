def rotate_matrix(matrix: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*matrix[::-1])]

if __name__ == "__main__":
    print(rotate_matrix([[1, 2], [3, 4]]))        # [[3, 1], [4, 2]]
    print(rotate_matrix([[1, 2, 3], [4, 5, 6]]))  # [[4, 1], [5, 2], [6, 3]]
    print(rotate_matrix([[1, 2, 3]]))             # [[1], [2], [3]]
    print(rotate_matrix([[1], [2], [3]]))         # [[3, 2, 1]]
    print(rotate_matrix([[7]]))                   # [[7]]
    print(rotate_matrix([]))                      # []
