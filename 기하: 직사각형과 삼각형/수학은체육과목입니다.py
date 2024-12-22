n = int(input())

circum = 0
for i in range(1,n+1):
  circum += 3
  if i == n:
    circum += n
print(circum)

# version 2
n = int(input())

print(4*n)