class TrieNode:

    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        root = TrieNode()
        for word in words:
            root.addWord(word)

        visit = set()
        res = set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r >= m or
                c >= n or (r, c) in visit or
                board[r][c] not in node.children
            ):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))

        for r in range(m):
            for c in range(n):
                dfs(r, c, root, "")
        return list(res)