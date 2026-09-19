# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root :
            return 0
        max_sum = float('-inf')
        def traverse(root):
            nonlocal max_sum
            if not root:
                return 0
            
            mps_left = max(traverse(root.left), 0)
            mps_right = max(traverse(root.right), 0)
            max_sum = max(max_sum, root.val + mps_left + mps_right)
            print(max_sum)
            # mps_root = max(mps_left, mps_right, max_branch_l + max_branch_r + root.val)
            # max_branch = max(max(0, max_branch_l + root.val), max(0, max_branch_r + root.val))

            return root.val + max(mps_left, mps_right)
        
        traverse(root)
        return max_sum
        
            