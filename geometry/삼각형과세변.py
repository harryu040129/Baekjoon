def isTriangle(li):
  sum = 0
  max = 0
  for x in li:
    if x > max:
      max = x
    sum += x
  sum -= max
  if max<sum:
    return whichTri(li) 
  else:
    return "Invalid"

def whichTri(li):
  if li[0] == li[1] and li[1] == li[2]:
    return "Equilateral"
  elif li[0] == li[1] or li[1] == li[2] or li[0] == li[2]:
    return "Isosceles"
  else:
    return "Scalene"

while True:
  li = list(map(int,input().split()))
  if li[0] + li[1] + li[2] == 0:
    break
  print(isTriangle(li))
