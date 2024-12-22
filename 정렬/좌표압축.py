import sys

n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

so = sorted(set(li))

dic = {so[i]:i for i in range(len(so))}

for x in li:
  print(dic[x], end=' ')