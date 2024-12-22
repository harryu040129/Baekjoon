import sys

n = int(sys.stdin.readline())

li = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    li.append((x, y))

li = sorted(li, key=lambda x: (x[1], x[0]))

for x in li:
    print(x[0], x[1])