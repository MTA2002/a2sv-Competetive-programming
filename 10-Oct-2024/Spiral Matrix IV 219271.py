# Problem: Spiral Matrix IV - https://leetcode.com/problems/spiral-matrix-iv/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        directions = {'EAST': (0, 1), 'SOUTH': (1, 0), 'NORTH': (-1, 0), 'WEST': (0, -1)}
        next_direction = {'EAST': 'SOUTH', 'SOUTH': 'WEST', 'WEST': 'NORTH', 'NORTH': 'EAST'}
        current_direction = 'EAST'

        grid = [[-1] * n for _ in range(m)]
        current_row, current_col = 0, 0

        while head:
            grid[current_row][current_col] = head.val
            head = head.next

            new_row = current_row +  directions[current_direction][0]
            new_col = current_col +  directions[current_direction][1]

            if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == -1:
                current_row = new_row
                current_col = new_col
            else:
                current_direction = next_direction[current_direction]
                current_row = current_row +  directions[current_direction][0]
                current_col = current_col +  directions[current_direction][1]
        
        return grid