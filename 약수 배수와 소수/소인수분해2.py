import math

N = int(input())

prime = [True for i in range(N+1)]
prime[0] = prime[1] = False

for i in range(2, int(math.sqrt(N))+1):
  if prime[i]:
    for j in range(2*i, int(math.sqrt(N))+1, i):
      prime[j] = False

for i in range(2,int(math.sqrt(N))+1):
  while prime[i] and N%i == 0:
    N/=i
    print(i)
if N>1:
  print(N)