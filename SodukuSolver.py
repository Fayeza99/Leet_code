class Solution:
    def solveSudoku(self, board):
        self.backtrack(board)

    def findEmpty(self, board):
        """
        Find an empty space in the board, empty spaces are represented by '.'
        Return a tuple (row, col) if an empty space is found, otherwise None.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    return (i, j)
        return None

    def isValid(self, board, guess, row, col):
        """
        Determine if a guess at a position is valid according to Sudoku rules.
        """
        # Row check
        if guess in board[row]:
            return False

        # Column check
        col_vals = [board[i][col] for i in range(len(board))]
        if guess in col_vals:
            return False

        # 3x3 square check
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == guess:
                    return False

        return True

    def backtrack(self, board):
        """
        Use backtracking to solve the Sudoku puzzle.
        """
        # Find an empty spot
        empty = self.findEmpty(board)
        if not empty:
            return True  # Puzzle solved
        else:
            row, col = empty

        for num in range(1, 10):
            if self.isValid(board, str(num), row, col):
                board[row][col] = str(num)

                if self.backtrack(board):
                    return True

                board[row][col] = '.'  # Reset if backtrack

        return False

def main():
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    
    solution = Solution()
    print("Original board:")
    for row in board:
        print(" ".join(row))
    
    solution.solveSudoku(board)
    
    print("\nSolved board:")
    for row in board:
        print(" ".join(row))

if __name__ == "__main__":
    main()
