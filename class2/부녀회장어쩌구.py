import sys
import copy

num = int(sys.stdin.readline())

for i in range(num):
  k = int(sys.stdin.readline())
  n = int(sys.stdin.readline())
  li_temp = [i for i in range(1,n+1)]
  li = [0]*n
  for j in range(k):
    for m in range(n):
      temp = sum(li_temp[0:m+1])
      li[m] = temp
    li_temp = copy.deepcopy(li)
  print(li[-1])
