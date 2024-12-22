import sys
from collections import Counter

n = int(sys.stdin.readline())
stack = [0]*n

for i in range(n):
  num = int(sys.stdin.readline())
  stack[i] = num

stack.sort()
print(int(sum(stack)/n+0.5))

print(stack[n//2])

if n == 1:
  print(stack[0])
else:
  counter = Counter(stack)
  temp = counter.most_common(2)
  if temp[0][1] == temp[1][1]:
    print(temp[1][0])
  else:
    print(temp[0][0])
print(stack[n-1]-stack[0])