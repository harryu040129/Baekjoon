import sys

sys.setrecursionlimit(10**7)

n = int(sys.stdin.readline().strip())

mat = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
  tmp = list(map(int, sys.stdin.readline().strip().split()))
  for idx, item in enumerate(tmp):
    if item == 1:
      mat[i][idx] = 1

# recursive function
def divide_conquer(mat, w, b):
  # for row in mat
  # for x in row
  # 두번 해야 전체 matrix 확인한다.
  if all(x == 0 for row in mat for x in row): 
      w += 1
      return w, b
  elif all(x == 1 for row in mat for x in row): 
      b += 1
      return w, b

  # len(mat) 사용해서 길이 다이나믹
  mid = len(mat)//2
  # pandas numpy slicing에 너무 익숙해져있었나봄..
  top_left = [row[:mid] for row in mat[:mid]]
  top_right = [row[mid:] for row in mat[:mid]]
  bottom_left = [row[:mid] for row in mat[mid:]]
  bottom_right = [row[mid:] for row in mat[mid:]]

  # Recursive calls
  w, b = divide_conquer(top_left, w, b)
  w, b = divide_conquer(top_right, w, b)
  w, b = divide_conquer(bottom_left, w, b)
  w, b = divide_conquer(bottom_right, w, b)

  return w, b

white, blue = divide_conquer(mat, 0, 0)
print(white)
print(blue)

