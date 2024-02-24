# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.counter = Counter()
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        def inorder(cur:Optional[TreeNode]):
            if cur:
                inorder(cur.left)
                self.counter[cur.val] += 1
                inorder(cur.right)

        inorder(root)

        max_count = max(self.counter.values())
        ans = [key for key,val in self.counter.items() if val == max_count]

        return ans
