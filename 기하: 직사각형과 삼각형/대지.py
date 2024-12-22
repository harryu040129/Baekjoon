n = int(input())
x = [0 for i in range(n)]
y = [0 for i in range(n)]

for i in range(n):
  x[i],y[i] = map(int, input().split())

min_x, min_y = 10000, 10000
max_x, max_y = -10000, -10000

for i in range(n):
  if x[i]>max_x:
    max_x = x[i]
  if x[i]<min_x:
    min_x = x[i]
  if y[i]>max_y:
    max_y = y[i]
  if y[i]<min_y:
    min_y = y[i]

lenx = max_x - min_x
leny = max_y - min_y

print(lenx*leny)
