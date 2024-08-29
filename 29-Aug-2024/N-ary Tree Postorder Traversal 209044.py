# Problem: N-ary Tree Postorder Traversal - https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        
        def postorderTraversal(current: 'Node'):
            if current!=None:
                for node in current.children:
                    postorderTraversal(node)
                ans.append(current.val)
        postorderTraversal(root)
        return ans