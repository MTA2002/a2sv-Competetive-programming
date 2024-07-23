# Problem: D - The Flip Tree - https://codeforces.com/gym/515998/problem/D

import sys
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
  n = ip()
  
  graph = defaultdict(list)
  
  for _ in range(n - 1):
    u , v = readList()
    graph[v].append(u)
    graph[u].append(v)

  init = readList()
  goal = readList()
  
  if init == goal:
    print(0)
    return
  stack = []
  stack.append((1 , 0 , 0 , 0))
  ans = set()
  visited = {1}
  
  while stack:
    vertex , even_flips , odd_flips , level = stack.pop()
    
    if level % 2 == 0:
      if even_flips % 2 == 0 and init[vertex - 1] != goal[vertex - 1]:
        ans.add(vertex)
        even_flips += 1
      elif even_flips % 2 == 1 and init[vertex - 1] == goal[vertex - 1]:
        ans.add(vertex)
        even_flips += 1
    else:
      if odd_flips % 2 == 0 and init[vertex - 1] != goal[vertex - 1]:
        ans.add(vertex)
        odd_flips += 1
      elif odd_flips % 2 == 1 and init[vertex - 1] == goal[vertex - 1]:
        ans.add(vertex)
        odd_flips += 1
    
    
    for neigbor in graph[vertex]:
      if neigbor not in visited:
        visited.add(neigbor)
        stack.append((neigbor , even_flips, odd_flips , level + 1))
  
  print(len(ans))

  for a in ans:
    print(a)

# T = int(input())
T = 1

for _ in range(T):
  solve()




