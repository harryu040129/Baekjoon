import math

a,b,v = map(int, input().split())
sum = 0
cnt = 0
sum += a
cnt += 1
rest = (v-a)/(a-b)

print(math.ceil(cnt+rest))