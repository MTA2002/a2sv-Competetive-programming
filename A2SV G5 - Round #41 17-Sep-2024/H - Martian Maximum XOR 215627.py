# Problem: H - Martian Maximum XOR - https://codeforces.com/gym/544854/problem/D

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

class TrieNode:
    def __init__(self):
        self.children = [None] * 2
        self.is_end = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, idx1):
        cur = self.root

        for ch in word:
            idx = int(ch)

            if cur.children[idx] == None:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        
        cur.is_end.append(idx1)
        
        
            

    def search(self, word):
        cur = self.root
        val = 0
        bit = len(word) - 1
        idx = 0

        for ch in word:
            ch = int(ch)

            if cur.children[ch]:
              val += 1 << bit
            
            
            # print(ch, cur.children[ch] == None)
            if cur.children[ch] == None: 
              cur = cur.children[0 if ch == 1 else 1]
            else:
              cur = cur.children[ch]
              
            if cur.is_end:
              idx = cur.is_end[0]
              # print(cur.is_end)

            bit -= 1
            
        # print(idx, val, word)
        return idx, val
    
def solve():
  n, k = readList()

  arr = readList()
  trie = Trie()     
  max_ = float('-inf')
  ans = [-1, -1]
  binary = bin(arr[0])[2:]
  binary = (k - len(binary)) * '0' + binary
  trie.insert(binary, 0)

  for idx, a in enumerate(arr):
    if idx > 0:
      binary = bin(a)[2:]
      binary = (k - len(binary)) * '0' + binary
      idx1, value = trie.search(binary)

      if value > max_:
        ans[0] = idx + 1
        ans[1] = idx1 + 1
        max_ = value
      
      trie.insert(binary, idx)

  binary = bin(arr[ans[0] - 1])[2:]
  binary = (k - len(binary)) * '0' + binary
  binary1 =  bin(arr[ans[1] - 1])[2:]
  binary1 = (k - len(binary1)) * '0' + binary1

  binary = binary[::-1]
  binary1 = binary1[::-1]
  x_or = 0

  for i in range(len(binary)):
     if binary[i] == binary1[i] == '0':
        x_or |= 1 << i

  print(*ans, x_or)


      
T = 1
T = int(input())
for _ in range(T):
  solve()