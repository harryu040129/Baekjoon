N = int(input())

li = []
n_5 = 0
n_3 = 0
while True:
  if n_5*5 > N:
    break
  res = 0
  for i in range(n_5):
    res += 5
  while res < N:
    res += 3
    n_3 += 1
  if res == N:
    li.append(n_3+n_5)
  n_5 += 1
  n_3 = 0
if li:
  print(min(li))
else:
  print(-1)