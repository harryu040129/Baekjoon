import sys
n = int(sys.stdin.readline())

li = [(0,0)] * n

for i in range(n):
  temp = tuple(map(int, sys.stdin.readline().split()))
  li[i] = temp
i = 0
li = sorted(li, key = lambda x : x[1])

while i < n:
    a = i
    while i + 1 < n and li[i][1] == li[i + 1][1]:
        i += 1
    b = i + 1
    li[a:b] = sorted(li[a:b], key=lambda x: x[0])
    i = b

for x in li:
  print(*x)