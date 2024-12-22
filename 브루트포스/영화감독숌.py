N = int(input())
cnt = 1
res = 666
while True:
  res += 1
  if "666" in str(res):
    cnt += 1
  if cnt == N:
    break
if N == 1:
  print(666)
else:
  print(res)