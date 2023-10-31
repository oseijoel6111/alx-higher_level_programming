#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N non-attacking queens on an NxN chessboard.

Usage: nqueens N
If the user called the program with the wrong number of arguments, print Usage: nqueens N, followed by a new line, and exit with the status 1
where N must be an integer greater or equal to 4
If N is not an integer, print N must be a number, followed by a new line, and exit with the status 1
If N is smaller than 4, print N must be at least 4, followed by a new line, and exit with the status 1
The program should print every possible solution to the problem
One solution per line
Format: see example
You don’t have to print the solutions in a specific order
You are only allowed to import the sys module
"""

import sys

def is_safe(board, row, col):
    """Check if it's safe to place a queen at a given position."""
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True

def print_solution(board):
    """Print a solution in the required format."""
    for row in board:
        print("[" + str(board.index(row)) + ", " + str(row) + "]", end="")
        if board.index(row) < len(board) - 1:
            print(", ", end="")
    print()

def solve_nqueens(n):
    """Solve the N-Queens puzzle and print all solutions."""
    def backtrack(col):
        if col == n:
            solutions.append(board[:])
            return
        for row in range(n):
            if is_safe(board, row, col):
                board.append(row)
                backtrack(col + 1)
                board.pop()

    solutions = []
    board = []
    backtrack(0)
    for solution in solutions:
        print_solution(solution)

if __name__ == "__main":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(n)
