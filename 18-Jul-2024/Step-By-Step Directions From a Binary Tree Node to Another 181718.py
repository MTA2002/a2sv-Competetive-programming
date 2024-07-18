# Problem: Step-By-Step Directions From a Binary Tree Node to Another - https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        graph = defaultdict(list)

        def preOrder(cur):
            if cur:
                if cur.left:
                    graph[cur.left.val].append((cur.val, 'U'))
                    graph[cur.val].append((cur.left.val, 'L'))
                
                if cur.right:
                    graph[cur.right.val].append((cur.val, 'U'))
                    graph[cur.val].append((cur.right.val, 'R'))
                
                preOrder(cur.left)
                preOrder(cur.right)
        
        
        preOrder(root)

        queue = deque()
        queue.append((startValue, ''))
        visited = {startValue}
        path = {}
        path[(startValue, '')] = -1

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                if node[0] == destValue:
                    final_path = []

                    while node != -1:
                        final_path.append(node[1])
                        node = path[node]
                    
                    return ''.join(final_path[::-1])
                
                for neighbor in graph[node[0]]:
                    if neighbor[0] not in visited:
                        visited.add(neighbor[0])
                        queue.append(neighbor)
                        path[neighbor] = node