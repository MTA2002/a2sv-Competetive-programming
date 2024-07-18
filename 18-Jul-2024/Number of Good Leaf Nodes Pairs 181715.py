# Problem: Number of Good Leaf Nodes Pairs - https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        paths = []

        def preorder(cur, path, level, idx):
            if cur:
                path.append((level, idx))

                if not cur.left and not cur.right:
                    paths.append(path[:])

                preorder(cur.left, path, level + 1, 2 * idx)
                preorder(cur.right, path, level + 1, 2 * idx + 1)
                path.pop()
        
        preorder(root, [], 0, 0)

        def calculateDistance(path1, path2):
            i = 0

            while i < min(len(path1), len(path2)):
                if path1[i] != path2[i]:
                    break
                i += 1

            return (len(path1) - i) + (len(path2) - i)

        ans = 0

        for i in range(len(paths)):
            for j in range(i + 1, len(paths)):
                if calculateDistance(paths[i], paths[j]) <= distance:
                    ans += 1

        return ans