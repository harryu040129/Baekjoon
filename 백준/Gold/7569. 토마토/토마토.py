import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())
graph = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

# 방향 설정
dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

# BFS
queue = deque()
all_ripe = True
has_ripe = False

for i in range(H):
  for j in range(N):
    for k in range(M):
      if graph[i][j][k] == 1:
        has_ripe = True
        queue.append((i, j, k))
      elif graph[i][j][k] == 0:
        all_ripe = False

# BFS 함수
def BFS():
  while queue:
    z, x, y = queue.popleft()
    for i in range(6): # 모든 방향 고려
      nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]
      # range 만족하면서 0일때
      if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M and graph[nz][nx][ny] == 0:
        graph[nz][nx][ny] = graph[z][x][y] + 1
        queue.append((nz, nx, ny))

# 모든 토마토가 익어있는 상태일때
if all_ripe:
  print(0)
  sys.exit()

# 익은 토마토가 없을때
if not has_ripe:
  print(-1)
  sys.exit()

BFS()

day = 0
for i in range(H):
  for j in range(N):
    for k in range(M):
      # BFS 다 돌았는데 아직도 0이 있으니까 
      # 토마토가 다 익지는 못하는 상황이다.
      if graph[i][j][k] == 0:
        print(-1)
        sys.exit()
      day = max(day, graph[i][j][k])

print(day - 1)