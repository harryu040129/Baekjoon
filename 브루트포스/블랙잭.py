import sys

N,M = map(int,input().split())
li = list(map(int,input().split()))
max = sys.maxsize
for i in range(len(li)):
  for j in range(i+1,len(li)):
    for k in range(j+1, len(li)):  
      temp = li[i] + li[j] + li[k]
      if abs(temp-M) < abs(max-M) and temp<=M:
        max = temp
print(max)