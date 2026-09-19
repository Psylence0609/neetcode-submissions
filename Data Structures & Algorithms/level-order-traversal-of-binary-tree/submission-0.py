# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append([root])
        result = [[root.val]]
        while queue:
            nodes = queue.popleft()
            level = []
            for node in nodes:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            if len(level):
                queue.append(level)
                result.append([x.val for x in level])
        return result