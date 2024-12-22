import sys
n = sys.stdin.readline()

li = []

for x in n:
  li.append(x)

li = sorted(li)[::-1]

for x in li:
  print(x,end = "")