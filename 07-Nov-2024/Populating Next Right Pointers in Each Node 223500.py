# Problem: Populating Next Right Pointers in Each Node - https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = deque()
        
        if root:
            queue.append(root)

        while queue:
            prev = None

            for _ in range(len(queue)):
                cur_node = queue.popleft()

                if prev:
                    prev.next = cur_node
                
                prev = cur_node

                if cur_node.left:
                    queue.append(cur_node.left)
                
                if cur_node.right:
                    queue.append(cur_node.right)
        
        return root