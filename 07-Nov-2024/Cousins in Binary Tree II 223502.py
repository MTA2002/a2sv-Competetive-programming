# Problem: Cousins in Binary Tree II - https://leetcode.com/problems/cousins-in-binary-tree-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque()
        queue.append(root)
        cur_level_sum = root.val
        root.val *= -1

        while queue:
            next_level_sum = 0

            for _ in range(len(queue)):
                node = queue.popleft()
                node.val = cur_level_sum + node.val

                if node.left and node.right:
                    next_level_sum += node.left.val
                    next_level_sum += node.right.val
                    node.left.val , node.right.val = -(node.left.val + node.right.val), -(node.right.val + node.left.val)
                    queue.append(node.left)
                    queue.append(node.right)
                elif node.left:
                    queue.append(node.left)
                    next_level_sum += node.left.val
                    node.left.val *= -1
                elif node.right:
                    queue.append(node.right)
                    next_level_sum += node.right.val
                    node.right.val *= -1

            cur_level_sum = next_level_sum
        
        return root