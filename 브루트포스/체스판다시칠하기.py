def createboard(M,i=0):
  line = ""
  if i%2 == 0:
    line = ("WB"*(int(M/2)))
  else:
    line = ("BW"*(int(M/2)))
  if M%2 == 1:
    line += line[0]
  return line

N,M = map(int, input().split())

check1, check2 = 0,0
a,b = 0,1
for i in range(N):
  l = input()
  line1, line2 = createboard(M,a), createboard(M,b)
  for j in range(M):
    if l[j] != line1[j]:
      check1 += 1
    if l[j] != line2[j]:
      check2 += 1
  a+=1
  b+=1

print(check1, check2)


