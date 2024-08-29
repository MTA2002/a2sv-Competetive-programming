# Problem: G - Small Town - https://codeforces.com/gym/543431/problem/G

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
  arr = readList()
  arr.sort()

  def checker(time):
    count = 1
    point = arr[0] + time

    for i in range(1, n):
      if abs(arr[i] - point) > time:
        count += 1
        point = arr[i] + time
    
    return count <= 3
  
  left = 0
  right = 10 ** 9

  while left <= right:
    mid = (left + right) // 2

    if checker(mid):
      right = mid - 1
    else:
      left = mid + 1
  
  print(left)

      
T = 1
T = int(input())
for _ in range(T):
  solve()