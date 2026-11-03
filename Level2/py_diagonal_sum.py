def diagonal_sum(matrix: list[list[int]]) -> int:
    total = 0
    n = len(matrix)
    for i in range(n):
        total += matrix[i][i]
        if i != n - 1 - i:
            total += matrix[i][n - 1 - i]
    return total

def main():
    print(diagonal_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # 25
    print(diagonal_sum([[1, 2], [3, 4]]))                   # 10
    print(diagonal_sum([[5]]))                              # 5
    print(diagonal_sum([[-1, 0], [0, -1]]))                 # -2
    print(diagonal_sum([]))                                 # 0

main()
