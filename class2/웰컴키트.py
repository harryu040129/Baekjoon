import sys
import math

N = int(sys.stdin.readline())
li = map(int, sys.stdin.readline().split())
T,P = map(int,sys.stdin.readline().split())

tshirt = 0

for x in li:
    if x > 0:
        tshirt += math.ceil(x / T)

pen = N//P
left = N-pen*P

print(tshirt)
print(pen,left)