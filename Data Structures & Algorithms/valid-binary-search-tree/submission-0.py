# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def checkValid(root, min_val, max_val) -> bool:
            if root is None: 
                return True
            # return true / False
            if (not checkValid(root.left, min_val, root.val) or not checkValid(root.right, root.val, max_val)):
                return False

            if root.val > min_val and root.val < max_val:
                return True
            
        
        return checkValid(root, -1000000001, 1000000001)
            

            