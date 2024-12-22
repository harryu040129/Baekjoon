import sys

def div(N):
  li = []
  while N != 0:
    temp = N%10
    N = N//10
    li.append(temp)
  li = li[::-1]
  return li

def sum(li):
  sum = 0
  for x in li:
    sum += x
  return sum

N = int(sys.stdin.readline())
li_ = div(N)

num = N - len(li_)*9
while True:
  li = div(num)
  summation = num + sum(li)
  if summation == N:
    break
  num += 1

print(num)