# Problem: The Two Routes - https://codeforces.com/problemset/problem/601/A

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
  n , m = readList()
  railway = defaultdict(list)

  for _ in range(m):
    u, v = readList()
    u -= 1
    v -= 1
    railway[u].append(v)
    railway[v].append(u)
  
  road = defaultdict(list)

  for u in range(n):
    for v in range(u + 1, n):
      if v not in railway[u]:
        road[u].append(v)
        road[v].append(u)
  
  
  def bfs(start, graph):
    queue = deque([start])
    visited = {start}
    level = 1
    cur_cost = [inf] * n
    cur_cost[start] = 0
    parents = {i:-1 for i in range(n)}

    while queue:
      for _ in range(len(queue)):
        node = queue.popleft()
        cur_cost[node] = min(cur_cost[node], level)

        for neighbor in graph[node]:
          if neighbor not in visited:
            parents[neighbor] = node
            visited.add(neighbor)
            queue.append(neighbor)
        
      level += 1

    path = []
    cur = n - 1
    
    while parents[cur] != -1:
      path.append(cur)
      cur = parents[cur]
    
    path.append(cur)

    return (path[::-1], cur_cost)

  train, train_cost = bfs(0, railway)
  bus, bus_cost = bfs(0, road)
  
  if 0 not in train or 0 not in bus:
    print(-1)
    return
  

  print(max(len(train), len(bus)) - 1)
     

  
      
T = 1
# T = int(input())
for _ in range(T):
 solve()