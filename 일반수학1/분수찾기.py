# 1    2   3   4   5   6   7   8   9   
# 1/1 1/2 2/1 3/1 2/2 1/3 1/4 2/3 3/2
# 0,0 1,0 0,1 0,2 1,1 2,0 3,0 2,1 1,2 0,3 0,4 1,3
n = int(input())
arr = []
for i in range(n):
  temp = []
  for j in range(n):
    temp.append(("{}/{}".format(i+1,j+1)))
  arr.append(temp)

