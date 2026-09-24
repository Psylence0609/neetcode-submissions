# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def serialize(self, root):
        result = []
        def dfs(node):
            if node is None:
                result.append("#")
                return
            result.append("$")
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return "".join(result)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        serialized_root = self.serialize(root)
        serialized_subRoot = self.serialize(subRoot)
        # print(serialized_root)
        # print(serialized_subRoot)
        return True if serialized_subRoot in serialized_root else False