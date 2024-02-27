# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def inorder(cur1,cur2):
            if cur1 and cur2:
                cur1.val += cur2.val

                if not cur1.left and cur2.left:
                    cur1.left = cur2.left
                    cur2.left = 0
                
                if not cur1.right and cur2.right:
                    cur1.right = cur2.right
                    cur2.right = 0

                inorder(cur1.left,cur2.left)
                inorder(cur1.right,cur2.right)
        
        if not root1 and root2:
            root1 = TreeNode()
        
        if not root2 and root1:
            root2 = TreeNode()

        inorder(root1,root2)

        return root1

