# Problem: G - MEX Tree Labeling - https://codeforces.com/gym/544853/problem/E

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
  graph = defaultdict(list)
  indegree = defaultdict(int)
  edges = []

  for i in range(n - 1):
    u, v = readList()
    edges.append((u, v, i))
    graph[v].append(u)
    graph[u].append(v)
    indegree[u] += 1
    indegree[v] += 1
  
  queeue = deque()
  sizes = [1] * n

  for i in range(1, n + 1):
    if indegree[i] == 1:
      queeue.append(i)
  

  while queeue:
    node = queeue.popleft()
    for neighbor in graph[node]:
      indegree[neighbor] -= 1
      if indegree[neighbor] == 1:
        queeue.append(neighbor)
        sizes[neighbor - 1] += sizes[node - 1]
      elif indegree[neighbor] > 1:
        sizes[neighbor - 1] += sizes[node - 1]

  temp = []

  for u, v, idx in edges:
    size = min(sizes[u - 1], sizes[v - 1])
    temp.append((u, v, idx, size * (n - size)))
  
  temp.sort(key= lambda x:x[3])

  ans = defaultdict(int)

  for i in range(n - 1):
    ans[temp[i][2]] = i
  
  for i in range(n - 1):
    print(ans[i])



T = 1
# T = int(input())
for _ in range(T):
  solve()