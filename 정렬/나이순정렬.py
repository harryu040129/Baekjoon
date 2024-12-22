import sys
n = int(sys.stdin.readline())

li = [[0,0,i] for i in range(n)]

for i in range(n):
  x,y = sys.stdin.readline().split()
  li[i][0] = int(x)
  li[i][1] = y

li = sorted(li, key = lambda x:(x[0], x[2]))

for x in li:
  print(x[0],x[1])