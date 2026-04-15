# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        # max(diameter, left + right)
        
        l_depth = 0 
        r_depth = 0

        if root.right:
            st = deque([(root.right, 1)])
            while st:
                node, depth = st.pop()

                if node.left:
                    st.append((node.left, depth+1))
                
                if node.right:
                    st.append((node.right, depth+1))
                
                r_depth = max(r_depth, depth)
        
        if root.left:
            st = deque([(root.left, 1)])
            while st:
                node, depth = st.pop()

                if node.left:
                    st.append((node.left, depth+1))
                
                if node.right:
                    st.append((node.right, depth+1))
                
                l_depth = max(depth, l_depth)

        return max(self.diameterOfBinaryTree(root.right), self.diameterOfBinaryTree(root.left), l_depth + r_depth)
        