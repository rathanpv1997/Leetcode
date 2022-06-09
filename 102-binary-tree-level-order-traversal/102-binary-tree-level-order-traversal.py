# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return []
        res.append([root.val])
        q = deque()
        q.append(root)
        while q:
            cur = []
            for i in range(len(q)):
                node = q.popleft()
                if not node.left and not node.right:
                    continue
                if node.left:
                    cur.append(node.left)
                if node.right:
                    cur.append(node.right)
            if not q and cur:
                res.append([node.val for node in cur])
            for n in cur:
                q.append(n)
        return res
        