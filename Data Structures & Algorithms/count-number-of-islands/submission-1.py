class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        def dfs(i, j):
            if (i<0 or j < 0 or i >= rows or j >= cols or grid[i][j] != '1'):
                return
            
            grid[i][j] = '-1'
            for di, dj in [(0, -1), (-1, 0), (1,0), (0, 1)]:
                ni, nj = i + di, j + dj
                dfs(ni, nj)
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)
        # print(grid)
        return count