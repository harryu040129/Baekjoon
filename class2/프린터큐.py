from collections import deque
import sys

queue = deque()

n = int(sys.stdin.readline())

for i in range(n):
  a,b = map(int, sys.stdin.readline().split())
  li = list(map(int, sys.stdin.readline().split()))
  queue.clear()
  for x in li:
    queue.append([x])
  temp = queue[b]
  cnt = 1
  while True:
    if max(queue) == temp and queue[0] == temp:
       print(cnt)
       break
    else:
       queue.rotate(-1)


