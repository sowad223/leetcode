class Solution(object):
    def largestIsland(self, grid):
        n = len(grid)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        sizes, current_id = {}, 2

        def dfs(i, j, id):
            if i < 0 or j < 0 or i >= n or j >= n or grid[i][j] != 1:
                return 0
            grid[i][j] = id
            return 1 + sum(dfs(i + dx, j + dy, id) for dx, dy in directions)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    sizes[current_id] = dfs(i, j, current_id)
                    current_id += 1

        max_size = max(sizes.values()) if sizes else 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set()
                    for dx, dy in directions:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] > 1:
                            seen.add(grid[ni][nj])
                    max_size = max(max_size, 1 + sum(sizes[id] for id in seen))

        return max_size or n * n
