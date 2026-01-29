# Overview:
#   if 'M' Mine square: replace Click with 'X'
#
#   Recursive loop: 
#       if 'E' Empty square + NO adject 'M' Mine:
#           replace with 'B'
#       if 'E' Empty square + adject 'M' Mine:
#           replace with '1-8'
#
# Inputs:
#   2D Array: Board
#       'M' - Mine / Bomb (unrevealed)
#       'X' - Exploded Mine / Bomb (revealed)
#
#       'E' - Unrevealed Empty / Unopened
#       'B' - Revealed Empty / opened
#
#       '1-8' - Int # of bomb adjacent
#
#   2e Array (Tuple): CLick pos  Click_x, Click_y
#       (Next click on unrevealed square: 'M' or 'E')
#
# Outputs:
#   2D Array: Board with new reveals


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        Cx, Cy = click
        currCellPos = board[Cx][Cy]

        # Base Case
        if (currCellPos == 'M'): 
            board[Cx][Cy] = 'X'
            return board


        # Recursive func: cell = tuple of coords
        def reveal(cellPos):
            currX, currY = cellPos
            rows, cols = len(board), len(board[0])

            # Adjcent cells global values
            adjGrid = [
                    (currX-1, currY-1), (currX, currY-1), (currX+1, currY-1), 
                    (currX-1, currY), (currX+1, currY), 
                    (currX-1, currY+1), (currX, currY+1),(currX+1, currY+1)
            ]
            
            bombCount = 0
            recurList = []

            # Loop through cells
            for nx, ny in adjGrid:
                if not (0 <= nx < rows and 0 <= ny < cols): # Check if cells are within bounds
                    continue
                
                if (board[nx][ny] == 'M'): bombCount += 1 # Increment for each surrounding bomb
                elif (board[nx][ny] == 'E'): recurList.append((nx, ny)) # Add Unrevealed to recur
            
            if (bombCount > 0): 
                board[currX][currY] = str(bombCount) # Set current cell to digit
            elif (bombCount == 0):
                board[currX][currY] = 'B' # Set current cell to revealed
                for cell in recurList:
                    reveal(cell)

        if (currCellPos == 'E'):
            reveal((Cx, Cy))

        return board
