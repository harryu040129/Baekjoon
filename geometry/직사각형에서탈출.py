import sys

x,y,w,h = map(int, input().split())

res = []
res.append(x)
res.append(y)
res.append(w-x)
res.append(h-y)

min = sys.maxsize

for element in res:
  if element<min:
    min = element

print(min)