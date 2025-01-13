import sys

N, M, B = map(int, sys.stdin.readline().split())

field = []

for _ in range(N):
  temp = map(int, sys.stdin.readline().strip().split())
  field.append([x for x in temp])

ans = int(1e10)
ground = 0

for i in range(256+1): # i: ground level
  use = 0
  take = 0
  for x in range(N):
    for y in range(M):
      if field[x][y] > i:
        take += field[x][y] - i # i로 맞추기
      else:
        use += i - field[x][y] # i로 맞추기
  if use>take+B:
    continue # 쓸수 있는 블록 개수 초과
  cnt = take * 2 + use

  if cnt <= ans:
    ans = cnt
    ground = i

print(ans, ground)