# Problem: Rotting Oranges
# Link: https://leetcode.com/problems/rotting-oranges/
# Note: BFS

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        fresh_cnt = 0
        rotten_coords = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten_coords.append((r, c))
                elif grid[r][c] == 1:
                    fresh_cnt += 1

        minutes = 0
        DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while rotten_coords and fresh_cnt:
            minutes += 1
            for _ in range(len(rotten_coords)):
                r, c = rotten_coords.popleft()

                for dr, dc in DIRS:
                    rr, cc = r + dr, c + dc
                    
                    if not(0 <= rr < rows and 0 <= cc < cols and grid[rr][cc] == 1):
                        continue

                    fresh_cnt -= 1
                    grid[rr][cc] = 2
                    rotten_coords.append((rr, cc))

        return minutes if not fresh_cnt else -1
