import sys

N, M = map(int, sys.stdin.readline().split())

li = list(map(int, sys.stdin.readline().split()))

start, end = 1, max(li)

while start <= end:
  summ = 0
  mid = (start+end)//2

  for item in li:
    if item > mid:
      summ += (item - mid)
  
  if summ < M:
    end = mid-1
  else:
    start = mid+1

print(end)