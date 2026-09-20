class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        complete = [0] * numCourses
        graph = {i: [] for i in range(numCourses)}
        visited = set()

        for i, j in prerequisites:
            graph[i].append(j)
        
        def dfs(x):
            if complete[x]:
                return True
            if x in visited:
                return False
            visited.add(x)
            for nxt in graph[x]:
                if dfs(nxt) == False:
                    return False
            complete[x] = 1
            return True
        
        for course in graph:
            dfs(course)
        
        return sum(complete) == numCourses