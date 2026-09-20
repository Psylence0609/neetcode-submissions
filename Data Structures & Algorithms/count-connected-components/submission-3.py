class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        visit = set()

        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for nxt in graph[node]:
                    dfs(nxt)
        counter = 0
        for node in graph:
            if node not in visit:
                counter += 1
                dfs(node)
        return counter