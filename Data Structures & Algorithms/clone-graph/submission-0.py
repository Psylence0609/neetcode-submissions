"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        queue = deque([node])
        val_mp = {}
        while queue:
            curr = queue.popleft()
            if curr.val not in val_mp:
                adj = []
                for neighbour in curr.neighbors:
                    if neighbour.val not in val_mp:
                        queue.append(neighbour)
                    adj.append(neighbour.val)
                val_mp[curr.val] = adj
        
        node_mp = {}
        for val in val_mp:
            node_mp[val] = Node(val, None)
        
        for key in node_mp:
            curr = node_mp[key]
            adj = []
            for n in val_mp[key]:
                adj.append(node_mp[n])
            curr.neighbors = adj

        return node_mp[1]
            