from collections import deque
import sys

queue = deque()

n = int(sys.stdin.readline())

for i in range(n):
  li = list(sys.stdin.readline().split())
  if li[0] == 'push':
      queue.append(int(li[1]))
  if li[0] == 'pop':
    if queue:
       temp = queue.popleft()
       print(temp)
    else:
        print(-1)
  elif li[0] == 'size':
    print(len(queue))
  elif li[0] == 'empty':
    if len(queue) == 0:
      print(1)
    else:
      print(0)
  elif li[0] == 'front':
    if queue:
      print(queue[0])
    else:
      print(-1)
  elif li[0] == 'back':
    if queue:
      print(queue[-1])
    else:
      print(-1)  