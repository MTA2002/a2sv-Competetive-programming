# Problem: D - Maximum Number of Zeroes - https://codeforces.com/gym/514644/problem/D

from collections import Counter, defaultdict, deque
from decimal import Decimal
import sys

def Int():return int(sys.stdin.readline().strip())
def arr():return list(map(int, sys.stdin.readline().strip().split()))
def string():return sys.stdin.readline().strip()


def solve():
    # pass
    size = Int()
    num1 = arr()
    num2 = arr()
    res = Counter()
    tt =0
    for i in range(size):
        if num1[i] != 0:
            ind = Decimal(-1 * num2[i]) /Decimal( num1[i])
            res[ind] += 1
        elif num2[i] == 0:
            tt += 1
    mm =res.values()
    print(max(mm) + tt if mm else tt)

    



t = 1
for _ in range(t):
    solve()