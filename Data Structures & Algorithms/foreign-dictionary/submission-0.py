class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {ch: set() for word in words for ch in word}
        indegree = {ch: 0 for ch in graph}

        for i in range(len(words) - 1):
            first = words[i]
            second = words[i + 1]

            if len(first) > len(second) and first.startswith(second):
                return ""

            for ch1, ch2 in zip(first, second):
                if ch1 != ch2:
                    if ch2 not in graph[ch1]:
                        graph[ch1].add(ch2)
                        indegree[ch2] += 1
                    break

        queue = deque(ch for ch in indegree if indegree[ch] == 0)
        answer = []

        while queue:
            ch = queue.popleft()
            answer.append(ch)

            for neighbor in graph[ch]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return "".join(answer) if len(answer) == len(graph) else ""
