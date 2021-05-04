import numpy as np


def is_under_attack(x, y):
    """
        Checks if the position is safe or is under attack by other queens.
        :param x: row or queen
        :param y: col
        :return: True if is under_attack
    """

    for i in range(n):

        """checking if it's not the same queen"""
        if i == x:
            continue

        """
            - The first condition checks if no one is attacking from top 
              and down rows but same column. 
            - The second condition checks if it safe on the diagonals. The 
              trick is to find the slope between both the queens i.e 
              |x1 - x2| == |y1 - y2|  
        """
        if positions[i] == y or abs(x - i) == abs(y - positions[i]):
            return True

    return False


def solve_eight_queen(queen=0):
    """
        Finds the possible positions of the queen on the N * N Grid.
    """

    if queen == n:
        return True

    for i in range(n):

        if is_under_attack(queen, i):
            continue

        positions[queen] = i

        solved = solve_eight_queen(queen + 1)

        if not solved:
            positions[queen] = -1000
        else:
            return True

    return False


def show_board():
    """
        Prints the board with queens ..
    """

    EMPTY = '*'
    QUEEN = 'Q'

    board = np.full([n, n], EMPTY)

    for i, j in enumerate(positions):
        if j >= 0:
            board[i][j] = QUEEN

    print(board)


if __name__ == "__main__":

    print("================ N QUEEN'S PROBLEM ========================")

    n = int(input("N: "))

    positions = np.full(n, -1000)

    solve_eight_queen()

    print(positions)

    show_board()
