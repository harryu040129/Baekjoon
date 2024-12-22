# 1: 1
# 2~7: 6
# 8~19: 12
# 20~37: 18

def checker(n):
  num = 1
  cnt = 1
  while num < n:
    for i in range(cnt):
      num += 6
    cnt += 1
  return cnt

n = int(input())
print(checker(n))
    
