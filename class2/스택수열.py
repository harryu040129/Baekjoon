import sys

n = int(sys.stdin.readline())
stack = []
res = []
ans = True
temp = 0

for i in range(n):
  inp = int(sys.stdin.readline())
  while inp>temp:
    temp += 1
    stack.append(temp)
    res.append("+")
  if stack and inp == stack.pop():
    res.append("-")
  else:
    ans = False
    

if ans:
  for x in res:
    print(x)
else:
  print("NO")