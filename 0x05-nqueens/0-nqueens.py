#!/usr/bin/python3

import sys


def print_usage_and_exit():
    """Prints usage information and exits."""
    print("Usage: nqueens N")
    sys.exit(1)


def print_number_error_and_exit():
    """Prints an error message if the input is not a number and exits."""
    print("N must be a number")
    sys.exit(1)


def print_value_error_and_exit():
    """Prints an error message if the input number is less than 4 and exits."""
    print("N must be at least 4")
    sys.exit(1)


def solve_nqueens(N):
    """Solves the N Queens problem and returns all solutions."""
    def is_valid(board, row, col):
        """Checks if placing a queen at (row, col) is valid."""
        for i in range(row):
            if board[i][1] == col or \
               abs(board[i][1] - col) == abs(board[i][0] - row):
                return False
        return True

    def solve(row):
        """Recursively places queens and finds all solutions."""
        if row == N:
            solutions.append(list(board))
            return
        for col in range(N):
            if is_valid(board, row, col):
                board[row] = [row, col]
                solve(row + 1)
                board[row] = [-1, -1]

    solutions = []
    board = [[-1, -1] for _ in range(N)]
    solve(0)
    return solutions


def main():
    """Main function to handle input and print solutions."""
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        N = int(sys.argv[1])
    except ValueError:
        print_number_error_and_exit()

    if N < 4:
        print_value_error_and_exit()

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()


