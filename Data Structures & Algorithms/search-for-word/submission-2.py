class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = False
        m, n = len(board), len(board[0])
        visited = set()
        def dfs(curr, idx):
            nonlocal res
            i, j = curr
            if board[i][j] != word[idx]:
                return
            if idx == len(word) - 1:
                res = True
                return
            visited.add((i, j))
            if not res:
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited:
                        dfs((ni, nj), idx + 1)
            visited.remove((i, j))
        for i in range(m):
            for j in range(n):
                if not res:
                    dfs((i, j), 0)
        return res