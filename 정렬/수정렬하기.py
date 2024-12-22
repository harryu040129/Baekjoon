N = int(input())
li = []

for i in range(N):
  li.append(int(input()))

li = sorted(li)

for x in li:
  print(x)