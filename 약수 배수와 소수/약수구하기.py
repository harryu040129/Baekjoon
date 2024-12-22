def findFactor(n):
  fac = []
  for i in range(n//2):
    if n%(i+1) == 0:
      fac.append(i+1)
  fac.append(n)
  return fac

n,k = map(int,input().split())
li = findFactor(n)
if len(li) >= k:
  print(li[k-1])
else:
  print(0)