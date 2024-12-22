import sys

a, b = map(int, sys.stdin.readline().split())
li = []

for i in range(a):
  li.append(int(sys.stdin.readline()))

temp = 0
result = 0  
while True:
  res = 0
  temp += 1
  for x in li:
      res += x // temp
  if res >= b:  
    result = temp
  else:
    break  

print(result)