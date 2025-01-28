from typing import List

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows, cols = len(grid), len(grid[0])
        max_fish = 0
        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0:
                return 0
            fish = grid[i][j]
            grid[i][j] = 0
            for dx, dy in directions:
                fish += dfs(i + dx, j + dy)
            return fish
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] > 0:
 
                    max_fish = max(max_fish, dfs(i, j))

        return max_fish
        