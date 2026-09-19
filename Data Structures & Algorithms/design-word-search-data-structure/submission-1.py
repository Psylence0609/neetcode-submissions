class Node:
    def __init__(self):
        self.children = {}
        self.endWord = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Node()
            cur = cur.children[ch]
        cur.endWord = True

    def search(self, word: str) -> bool:
        def recurse(i, node):
            if i == len(word):
                return node.endWord
            ch = word[i]
            if ch == '.':
                for child in node.children:
                    if recurse(i + 1, node.children[child]):
                        return True
                return False
            if ch not in node.children:
                return False
            return recurse(i + 1, node.children[ch])
        return recurse(0, self.root)
