class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        graph = {i: [] for i in range(n)}

        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        visited = set()

        def dfs(node, par):
            if node in visited:
                return False
            visited.add(node)
            for nxt in graph[node]:
                if nxt == par:
                    continue
                if not dfs(nxt, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n
