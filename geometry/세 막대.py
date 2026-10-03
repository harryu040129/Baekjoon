def maxPerimeter(li):
  sum = 0
  max = 0
  for x in li:
    if x > max:
      max = x
    sum += x
  sum -= max
  if max<sum:
    return sum+max 
  else:
    while max>=sum:
      max-=1
    return sum+max

li = list(map(int,input().split()))

print(maxPerimeter(li))