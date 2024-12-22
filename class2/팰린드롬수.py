import sys

while True:
  n = int(sys.stdin.readline())
  if n == 0:
    break
  n = str(n)
  if n == n[::-1]:
    print('yes')
  else:
    print('no')