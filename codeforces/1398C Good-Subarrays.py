from collections import Counter


t = int(input())

for _ in range(t):
  n = int(input())
  word = list(map(int,input()))
  counter = Counter()
  counter[0] = 1
  sum_ = 0
  count = 0

  for i in range(n):
    sum_ += word[i]
    target = sum_ - i - 1

    if target in counter:
      count += counter[target]
    
    counter[target] += 1
  
  print(count)


