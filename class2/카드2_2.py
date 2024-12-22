import sys
from collections import deque

n = int(sys.stdin.readline())
li = deque()

for i in range(1,n+1):
  li.append(i)

while len(li) != 1:
  li.popleft()
  li.append(li.popleft())

print(li[0])