import sys

n = int(input())
A = [0]*n

for i in range(n):
  A[i] = int(sys.stdin.readline())

C = [0]*(max(A)+1)
S = [0]*(max(A)+1)
s = 0

for x in A:
  C[x] += 1

for i in range(len(C)):
  s += C[i]
  S[i] = s


result = [0 for i in range(n)]

for x in A[::-1]:
  idx = S[x]-1
  S[x]-=1
  result[idx] = x

for x in result:
  print(x)