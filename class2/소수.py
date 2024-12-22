import sys

n,m = map(int, sys.stdin.readline().split())

li = [False, False] + [True] * (m-1)

for i in range(2,m+1):
  if li[i]:
    if i>=n:
      print(i)
    for j in range(2*i, m+1, i):
        li[j] = False
