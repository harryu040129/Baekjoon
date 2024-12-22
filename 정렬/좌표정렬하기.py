import sys
n = int(sys.stdin.readline())

li = [(0,0)] * n

for i in range(n):
  temp = tuple(map(int, sys.stdin.readline().split()))
  li[i] = temp
i = 0
li = sorted(li)
print(li)
while i <= n:
  a = i
  if i == i+1:
    i+=1
  b = i
  print(a,b)
  li[a:b] = sorted(li[a:b], key = lambda x : x[1])
  i+=1
print(li)
for x in li:
  print(*x)
