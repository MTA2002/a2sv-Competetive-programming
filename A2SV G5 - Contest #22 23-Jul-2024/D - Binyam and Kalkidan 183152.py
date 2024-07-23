# Problem: D - Binyam and Kalkidan - https://codeforces.com/gym/531455/problem/D

import sys
import heapq
from math import ceil, inf, log2, floor
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
  nums = list(map(int, input()))
  ans = []
  
  all_answer = {
    2 : [2],
    3 : [3],
    4 : [2 , 2, 3],
    5 : [5],
    6 : [3, 5],
    7 : [7],
    8 : [2,2,2, 7],
    9 : [3,3,2,7]
  }
   
  for num in nums:
    if num > 1:
      ans.extend(all_answer[num])
  
  ans.sort(reverse=True)
  print(''.join(map(str, ans)))
T = 1
# T = int(input())
for _ in range(T):
  solve()