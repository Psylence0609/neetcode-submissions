# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        serial = []

        def inorder(root):
            if not root:
                return
            if len(serial) == k:
                return
            inorder(root.left)
            if len(serial) == k:
                return
            serial.append(root.val)
            if len(serial) == k:
                return
            inorder(root.right)
        inorder(root)
        print(serial)
        return serial[-1]