def createboard(j=0):
  li = []
  for i in range(8):
    if (i+j)%2 == 0:
      li.append(['W','B','W','B','W','B','W','B'])
    else:
      li.append(['B','W','B','W','B','W','B','W'])
  return li

board1 = createboard(0)
board2 = createboard(1)

N,M = map(int, input().split())
board = []
for i in range(N):
  board.append(list(map(str, input())))

def compare(board1, board, x, y):
  cnt = 0
  for i in range(8):
    for j in range(8):
      if board1[i][j] != board[x+i][y+j]:
        cnt += 1
  return cnt

res = 64
for i in range(N-7):
  for j in range(M-7):
    temp1 = compare(board1, board, i, j)
    temp2 = compare(board2, board, i, j)
    res = min(res,temp1,temp2)
  
print(res)

