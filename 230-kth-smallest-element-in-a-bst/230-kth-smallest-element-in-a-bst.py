# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.inorder(root)[k-1]
        
    def inorder(self,root):
        out = []
        if root.left:
            out += self.inorder(root.left)
        out = out + [root.val]
        if root.right:
            out += self.inorder(root.right)
        return out