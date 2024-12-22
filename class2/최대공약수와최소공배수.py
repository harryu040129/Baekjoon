import sys

a,b = map(int,sys.stdin.readline().split())
x = min([a,b])
max = 0

for i in range(1,x):
  if a%i == 0 and b%i == 0:
    max = i

i = a*b
min = 0
while i>=(a+b-x):
  if i%a == 0 and i%b == 0:
    min = i
  i-=1

print(max)
print(min)