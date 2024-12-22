a,b,c,d,e,f = map(int, input().split())
bo = False
x,y = 0,0
for i in range(-999,1000):
  for j in range(-999,1000):
    if a*i+b*j==c and d*i+e*j==f:
      if bo == True:
        bo = False
        break
      bo = True
      x,y = i,j

print(x,y)