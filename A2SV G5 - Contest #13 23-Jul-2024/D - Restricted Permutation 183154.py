# Problem: D - Restricted Permutation - https://codeforces.com/gym/519135/problem/D

import sys
import heapq
from math import ceil, inf
from collections import defaultdict , Counter, deque
from bisect import bisect_left , bisect_right
mod = pow(10, 9) + 7

def ip():
  return int(input())

def input():
  return sys.stdin.readline().strip()

def readList():
  return list(map(int,input().split()))

def solve():
    n , m = readList()
    
    graph = defaultdict(list)
    counter = Counter()
    
    for _ in range(m):
        a , b = readList()
        graph[a].append(b)
        counter[b] += 1

    queue = []
    
    for i in range(n):
        if counter[i + 1] == 0:
            heapq.heappush(queue , i + 1)
            
    order = []
    while queue:
        cu = len(queue)
        
        for _ in range(cu):
            c = heapq.heappop(queue)
            order.append(c)
            
            for neighbor in graph[c]:
                counter[neighbor] -= 1
                
                if counter[neighbor] == 0:
                     heapq.heappush(queue , neighbor)
    
    if len(order) != n:
        print(-1)
        return
        
    print(*order)
                    
                    
            



# T = int(input())
T = 1

for _ in range(T):
  solve()