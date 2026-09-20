class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        visit = set()

        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        def dfs(node, parent):
            if node in visit:
                return
            visit.add(node)
            for nxt in graph[node]:
                if nxt != parent:
                    dfs(nxt, node)
        counter = 0
        for node in graph:
            if node not in visit:
                counter += 1
                dfs(node, None)
        return counter