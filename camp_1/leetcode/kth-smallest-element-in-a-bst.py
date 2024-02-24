# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def inorder(current: Optional[TreeNode]):
            if current:
                inorder(current.left)
                arr.append(current.val)
                inorder(current.right)
        
        inorder(root)
        print(arr)

        return arr[k-1]


