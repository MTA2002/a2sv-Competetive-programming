# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        turn = time // (n - 1)
        time -= time // (n - 1) * (n - 1)

        return 1 + time if turn % 2 == 0 else n - time