from collections import deque
import sys

n,k = sys.stdin.readline().split()
queue = deque()

for i in range(1, int(n)+1):
  queue.append(i)

print("<", end="")

while queue:
  queue.rotate((int(k)-1)*-1)
  print(queue.popleft(), end = "")
  if queue:
    print(", ", end = "")
print(">")
