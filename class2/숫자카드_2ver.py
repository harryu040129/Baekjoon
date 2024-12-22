import sys

n = int(sys.stdin.readline())

dic = {}
li_origin = map(int, sys.stdin.readline().split())

for x in li_origin:
  if x in dic:
    dic[x] += 1
  else:
    dic[x] = 1

num = int(sys.stdin.readline())
li_try = map(int, sys.stdin.readline().split())

for x in li_try:
  if x in dic:
    print(dic[x], end = " ")
  else:
    print("0", end = " ")