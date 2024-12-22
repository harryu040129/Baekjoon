import sys

a,b = map(int, sys.stdin.readline().split())

M = set()
N = set()

for i in range(a):
  M.add(sys.stdin.readline().strip())
for j in range(b):
  N.add(sys.stdin.readline().strip())

MandN = list(M & N)
MandN.sort()
print(len(MandN))
for x in MandN:
  print(x)