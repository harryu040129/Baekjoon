def factor(a,b):
  if a%b == 0:
    return "multiple"
  elif b%a == 0:
    return "factor"
  else:
    return "neither"

while True:
  a,b = map(int, input().split())  
  if a == 0 and b == 0:
    break
  print(factor(a,b))
