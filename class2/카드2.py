import sys

def lastCard(n):
  if len(n) == 1:
    return n
  temp = n[2:] + n[1]
  return lastCard(temp)

n = int(sys.stdin.readline())
num = ""
for i in range(1,n+1):
  num += str(i)

print(lastCard(num))