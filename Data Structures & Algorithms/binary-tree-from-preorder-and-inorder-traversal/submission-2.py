# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder node left right
        # inorder lefe node right

        # 1 2 5 6 3 4
        # 5 2 6 1 3 4
        # 0 1 2 3 5 6 null 4
        # ans : 1 2 3 5 6 null 4

        # 1 2 3 4
        # 2 1 3 4
    
        # if not preorder:
        #         return None

        # root = TreeNode(preorder[0])

        # mid = inorder.index(root.val)

        # root.left = self.buildTree(
        #     preorder[1:mid + 1],
        #     inorder[:mid]
        # )

        # root.right = self.buildTree(
        #     preorder[mid + 1:],
        #     inorder[mid + 1:]
        # )

        # return root


        # positions = {val: i for i, val in enumerate(inorder)}
        # pre_idx = 0

        # def build(left, right):
        #     nonlocal pre_idx

        #     if left > right:
        #         return None

        #     val = preorder[pre_idx]
        #     pre_idx += 1

        #     root = TreeNode(val)
        #     mid = positions[val]

        #     root.left = build(left, mid - 1)
        #     root.right = build(mid + 1, right)

        #     return root

        # return build(0, len(inorder) - 1)
        

        positions = {val : i for i, val in enumerate(inorder)}
        pre_idx = 0

        def build(left, right):
            nonlocal pre_idx

            if left > right:
                return None
            
            val = preorder[pre_idx]
            pre_idx += 1

            root = TreeNode(val)
            mid = positions[val]

            root.left = build(left, mid-1)
            root.right = build(mid+1, right)

            return root
        
        return build(0, len(inorder) - 1)

            
            