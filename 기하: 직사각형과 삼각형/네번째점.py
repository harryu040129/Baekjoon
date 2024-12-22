a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = []

for i in range(2):
  if a[i] == b[i]:
    d.append(c[i])
  elif b[i] == c[i]:
    d.append(a[i])
  elif c[i] == a[i]:
    d.append(b[i])
  
for x in d:
  print(x, end=" ")