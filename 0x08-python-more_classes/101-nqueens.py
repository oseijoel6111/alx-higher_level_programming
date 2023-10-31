#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.
"""

import sys

def init_board(n):
    """Initialize an `n`x`n` sized chessboard with empty squares."""
    board = [[' ' for _ in range(n)] for _ in range(n)]
    return board

def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at a given position."""
    # Check the column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_nqueens(board, row, n, solutions):
    """Recursively solve the N-queens puzzle."""
    if row == n:
        solutions.append(["[" + str(i) + ", " + str(board[i].index('Q')) + "]" for i in range(n)])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 'Q'
            solve_nqueens(board, row + 1, n, solutions)
            board[row][col] = ' '

def main():
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

    board = init_board(n)
    solutions = []
    solve_nqueens(board, 0, n, solutions)

    for solution in solutions:
        print("\n".join(solution))

if __name__ == "__main__":
    main()
