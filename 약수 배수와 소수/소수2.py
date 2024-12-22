import math
import sys

M = int(input())
N = int(input())

prime = [True for i in range(N+1)]
prime[0] = False
prime[1] = False

for i in range(2, int(math.sqrt(N))+1):
  if prime[i] == True:
    j = 2
    while i*j <= N:
      prime[i*j] = False
      j += 1

sum = 0
cnt = 0
min = sys.maxsize
for i in range(M,N+1):
  if prime[i]:
    sum += i
    if min>i:
      min = i

if sum == 0:
  print(-1)
else:
  print(sum)
  print(min)