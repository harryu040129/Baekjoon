def getAngles():
  li = []
  for i in range(3):
    angle = int(input())
    li.append(angle)
  return defineTri(li)

def listSum(li):
  sum = 0
  for x in li:
    sum += x
  return sum

def defineTri(li):
  sum = listSum(li)
  if sum == 180:
    if li[0] == li[1] and li[1] == li[2]:
      return "Equilateral"
    elif li[0] == li[1] or li[1] == li[2] or li[2] == li[0]:
      return "Isosceles"
    else:
      return "Scalene"
  else:
    return "Error"

    

angles = getAngles()
print(angles)