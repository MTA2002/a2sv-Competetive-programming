from bisect import bisect_right
import sys

def input():
  return sys.stdin.readline().strip()

n = int(input())

arr = list(map(int,input().split()))
arr.sort()
q = int(input())

for _ in range(q):
  
  num = int(input())
  
  print(bisect_right(arr,num))
  
  
  




