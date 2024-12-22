import sys

num = int(sys.stdin.readline())

for i in range(num):
  parenthesis = input()
  balance = "YES"
  li = []

  for x in parenthesis:
    if x == "(":
      li.append(x)
    elif x == ")":
      if li:
        li.pop()
      else:
        balance = "NO"
        break
  else:
    if len(li) != 0:
      balance = "NO"
  print(balance)