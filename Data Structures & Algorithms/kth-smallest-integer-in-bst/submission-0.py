# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = -1
        cnt = 0
        def count(root, k):
            nonlocal res, cnt
            if root is None:
                return 0
            count(root.left, k)
            cnt += 1            
            if cnt == k:
                res = root.val

            count(root.right, k)

        
            return 0

        
        count(root, k)
        return res