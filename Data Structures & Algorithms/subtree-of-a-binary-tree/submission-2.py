# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSametree(r1, r2):
            if not r1 or not r2:
                return r1 == r2
            return (
                r1.val == r2.val
                and isSametree(r1.right, r2.right) 
                and isSametree(r1.left, r2.left)
            )

        if not root:
            return False

        if root.val == subRoot.val:
            if isSametree(root, subRoot):
                return True

        return (
            self.isSubtree(root.right, subRoot)
            or self.isSubtree(root.left, subRoot)
        )
        
        
        