# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        def height(root):
            if root is None:
                return 0 

            l = 0 
            r = 0
            if root.left is not None:
                l = max(l, height(root.left))
            if root.right is not None:
                r = max(r, height(root.right))

            h = max(l, r) + 1
            return h

        st = [root]
        while st:
            node = st.pop()
            left = 0
            right = 0
            if node.right is not None:
                right = height(node.right)
                st.append(node.right)
            
            if node.left is not None:
                left = height(node.left)
                st.append(node.left)
            
            if abs(right - left) > 1:
                return False
            
        return True
        
