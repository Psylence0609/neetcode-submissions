# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def check(self, root):
        if not root:
            return True, float('inf'), float('-inf')
        res_left, min_left, max_left = self.check(root.left)
        res_right, min_right, max_right = self.check(root.right)

        # if min_left == float('inf'):
        #     min_curr = root.val

        return res_left and res_right and (root.val > max_left) and root.val < min_right, min(root.val, min_left), max(root.val, max_right)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res, _, _ = self.check(root)
        return res