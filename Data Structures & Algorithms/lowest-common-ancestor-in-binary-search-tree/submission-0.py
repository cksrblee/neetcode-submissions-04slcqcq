# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_path = []
        q_path = []

        def find_path(node, target, path):
            if node is None:
                return False

            path.append(node)

            if node.val == target:
                return True

            if find_path(node.left, target, path):
                return True

            if find_path(node.right, target, path):
                return True

            path.pop()
            return False
        
        find_path(root, p.val, p_path)
        find_path(root, q.val, q_path)

        for p_node in p_path[::-1]:
            for q_node in q_path[::-1]:
                if p_node==q_node:
                    return p_node
                
        return root