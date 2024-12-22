import sys

n = int(sys.stdin.readline())
A = [0]*10001

for i in range(n):
  A[int(sys.stdin.readline())] += 1

for i in range(10001):
  if A[i] != 0:
    for _ in range(A[i]):
      print(i)
