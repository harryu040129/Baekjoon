import sys

a,b = map(int, sys.stdin.readline().split())
li = []

for i in range(a):
  li.append(int(sys.stdin.readline()))

start, end = 1, max(li)

result = 0

while start <= end:
  mid = (start+end) // 2
  res = 0

  for x in li:
    res += x//mid
  
  if res >= b:
    result = mid
    start = mid+1
  else:
    end = mid-1

print(result)