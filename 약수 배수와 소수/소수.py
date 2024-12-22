def primeNumber(a):
  if a == 1:
    return False
  for i in range(2,a//2):
    if a%i == 0:
      return False
  return True

def listPrime(li):
  cnt = 0
  for x in li:
    if primeNumber(x):
      cnt += 1
  return cnt

n = int(input())
if n>100:
  raise Exception
li = map(int, input().split())
print(listPrime(li))