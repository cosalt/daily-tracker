#
# Overview: Not solving -> Simply confirming if valid
#
# Inputs:
#   Board: 2D Array of strings
#   
# Ouputs:
#   bool: True = valid
#
# Notes:
#   Set row == row len : for i{for j}
#   Set col == col len : for i{for j[i]}
#   set box == box len


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        ### Helpers
        # row uses list comprehension to return current row ignoring '.'
        def row(matrix, i): return [x for x in matrix[i] if x != "."]
        # col uses list comprehension to return current col ignoring '.'
        def column(matrix, i): return [matrix[r][i] for r in range(9) if matrix[r][i] != '.']
        # box uses list comprehension to return current box using (row / 3) * 3 + (col / 3)
        def box(matrix, i):
            r = (i // 3) * 3
            c = (i % 3) * 3
            return [matrix[i][j] for i in range(r, r + 3) for j in range(c, c + 3) if matrix[i][j] != "."]

        for i in range(len(board)):
            if len(row(board, i)) != len(set(row(board, i))): return False
            if len(column(board, i)) != len(set(column(board, i))): return False
            if len(box(board, i)) != len(set(box(board, i))): return False

        return True