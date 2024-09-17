# Problem: F - Swapping - https://codeforces.com/gym/544853/problem/D

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
  n , x, m = readList()
  min_ = x
  max_ = x

  for _ in range(m):
    l, r = readList()

    if l <= min_ <= r:
      min_ = l
    
    if l <= max_ <= r:
      max_ = r
  
  print(max_ - min_ + 1)
      
T = 1
T = int(input())
for _ in range(T):
  solve()