# Problem: C - Filling the Plate - https://codeforces.com/gym/531455/problem/C

import sys
import heapq
from math import ceil, inf
from collections import defaultdict , Counter, deque
from bisect import bisect_left , bisect_right
import sys, threading
import random

mod = pow(10, 9) + 7
randint = random.randint(1, 1000000)

def ip():
  return int(input())

def input():
  return sys.stdin.readline().strip()

def readList():
  return list(map(int,input().split()))

def solve():
  k , n , m = readList()
  parellelpipe = []
  
  for _ in range(k):
    rectangle = []
    input()
    for _ in range(n):
      rectangle.append(list(input()))
      
    parellelpipe.append(rectangle)
  
  input() 
  
  x, y = readList() 
  
  directions = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]
  queue = deque()
  parellelpipe[0][x - 1][y - 1] = '#'
  queue.append((0, x - 1, y - 1))
  
  def inbound(index ,row, col):  
    return 0 <= index < k and 0 <= row < n and 0 <= col < m
  
  ans = 0
  while queue:
    index, row, col = queue.popleft()
    ans += 1
    
    for dk, dr, dc in directions:
      new_k = index + dk
      new_r = dr + row
      new_c = dc + col
      
      if inbound(new_k, new_r, new_c) and parellelpipe[new_k][new_r][new_c] == '.':
        parellelpipe[new_k][new_r][new_c] = '#'
        queue.append((new_k, new_r, new_c))
  
  print(ans)
T = 1
# T = int(input())
for _ in range(T):
  solve()