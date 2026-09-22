class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = [(0,1), (1, 0), (0, -1), (-1, 0)]
        idx = 0
        m, n = len(matrix), len(matrix[0])
        pos = [0, 0]
        res = []
        for _ in range(m * n):
            # print(pos)
            res.append(matrix[pos[0]][pos[1]])
            matrix[pos[0]][pos[1]] = 101
            tmp_x, tmp_y = pos[0] + directions[idx][0], pos[1] + directions[idx][1]

            if tmp_x >= m or tmp_y >= n or tmp_x <0 or tmp_y < 0 or matrix[tmp_x][tmp_y] == 101:
                idx = (idx + 1) % 4
                tmp_x, tmp_y = pos[0] + directions[idx][0], pos[1] + directions[idx][1]
            pos = [tmp_x, tmp_y]
        # print(pos)
        return res