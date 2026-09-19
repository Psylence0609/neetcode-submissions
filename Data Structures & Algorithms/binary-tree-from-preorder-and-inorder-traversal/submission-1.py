# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mp = {}
        for i, val in enumerate(inorder):
            mp[val] = i
        def build(root_index, in_l, in_r):
            # if len(preorder) == 0:
            #     return None
            if in_l > in_r:
                return None
            # print(root_index, in_l, in_r)
            root = preorder[root_index]
            if in_l == in_r:
                return TreeNode(root, None, None)

            node = TreeNode(root)
            node.left = build(root_index + 1, in_l, mp[root] - 1)
            node.right = build(root_index + mp[root] - in_l + 1, mp[root] + 1, in_r)
            return node 
        return build(0, 0, len(inorder) -1)