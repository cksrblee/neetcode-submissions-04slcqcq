# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        pivot = -101
        def dfs(root, pivot) -> int:
            if root is None:
                return 0
            res = 0
            
            if root.val >= pivot:
                res+= 1
                pivot = root.val
            
            res += dfs(root.left, pivot)
            res += dfs(root.right, pivot)
            return res
        
        return dfs(root, pivot)


        #   3
        #  3
        # 4 2

        # 2
        # -  4
        #   10  8
        #   - - 4