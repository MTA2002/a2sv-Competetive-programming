# Problem: D - Energy Crisis - https://codeforces.com/gym/511242/problem/D

n, p = list(map(int,input().split()))
p /= 100
p = 1 - p
arr = list(map(int,input().split()))

arr.sort(reverse=True)

def checker(energy):
  curr = 0
  
  for i in range(n):
    if arr[i] >= energy:
      curr += (arr[i] - energy) * p
    else:
      if energy - arr[i] > curr:
        return False
      curr -= energy - arr[i]

  return True

low, high = arr[-1], arr[0]

while (high - low) >= 10**(-6):
  mid = (low + high)/2

  if checker(mid):
    low = mid
  else:
    high = mid 

print(low)