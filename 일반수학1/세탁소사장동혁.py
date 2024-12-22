n = int(input())
li = [25,10,5,1]
res = ""
for i in range(n):
  change = int(input())
  for coin in li:
    temp = change//coin
    change -= temp*coin
    res += "{} ".format(temp)
  print(res)
  res = ""
  