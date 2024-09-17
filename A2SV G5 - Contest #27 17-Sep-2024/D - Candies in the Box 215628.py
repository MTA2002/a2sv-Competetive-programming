# Problem: D - Candies in the Box - https://codeforces.com/gym/538762/problem/D

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
  n = ip()

  def helper(k):
    total = n
    vasyas = 0
    while total > 0:
      
      vasyas += k if k < total else total
      total -= k if k < total else total
      total -= total // 10
    
    return vasyas * 2 >= n

  left , right = 1 , n

  while left <= right:
    mid = (left + right) // 2
    # print(mid, helper(mid))
    if helper(mid):
      right = mid - 1
    else:
      left = mid + 1
    
  
  print(left)

T = 1
# T = int(input())
for _ in range(T):
  solve()