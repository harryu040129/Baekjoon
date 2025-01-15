import sys
from collections import deque

N,M = map(int, sys.stdin.readline().split())

arr = []
for _ in range(N):
  temp = sys.stdin.readline().strip()
  temp_li = []
  for x in temp:
    temp_li.append(x)
  arr.append(temp_li)

visited = set()
visited_cnt = 0
queue = deque()

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def BFS():
  global visited_cnt
  while queue:
    x,y = queue.popleft()
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]

      if 0<=nx<M and 0<=ny<N and (nx,ny) not in visited:
        if arr[ny][nx]=='P' :
          visited_cnt+=1
        if arr[ny][nx] == 'X':
          continue
        visited.add((nx,ny))
        queue.append((nx,ny))

ans_cnt = 0
for i in range(N):
  for j in range(M):
    if arr[i][j] == 'I':
      queue.append((j,i))
      visited.add((j,i))
      BFS()
    elif arr[i][j] == 'P':
      ans_cnt += 1

if visited_cnt != 0:
  print(visited_cnt)
else:
  print('TT')