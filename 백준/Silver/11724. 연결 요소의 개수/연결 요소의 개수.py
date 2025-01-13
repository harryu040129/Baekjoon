import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

li = {i:[] for i in range(1, N+1)}

for _ in range(M):
  u,v = map(int, sys.stdin.readline().strip().split())
  li[u].append(v)
  li[v].append(u)

visited = set()

def BFS(graph, start):
  queue = deque([start])
  visited.add(start)

  while queue:
    node = queue.popleft()
    for neighbor in graph[node]:
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append(neighbor)
  
cnt=0
for i in range(1, N+1):
  if i not in visited:
    BFS(li, i)
    cnt+=1

print(cnt)