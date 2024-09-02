# Problem: Meaningless Operations - https://codeforces.com/problemset/problem/1110/C

import sys
import heapq
from math import ceil, inf, gcd
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

def get_factors(num):
  i = 2
  factors = set()

  while i * i <= num:
    if num % i == 0:
      factors.add(num // i)
      factors.add(i)
    
    i += 1
  
  return factors

def solve():
  n = ip()
  compliment = int(''.join(['0' if b == '1' else '1' for b in bin(n)[2:]]), 2)
  
  if compliment:
    print(gcd(compliment ^ n, compliment & n))
    return
  
  factors = get_factors(n)

  if factors:
    print(gcd(max(factors) ^ n, max(factors) & n))
    return
  
  print(1)

      
T = 1
T = int(input())
for _ in range(T):
  solve()