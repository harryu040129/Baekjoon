import sys
from collections import deque, defaultdict

n = int(sys.stdin.readline().strip())
li = map(int, sys.stdin.readline().split())

queue = deque()
dic = defaultdict(int)

max_length = 0

for x in li:
    queue.append(x)
    dic[x] += 1
    
    # 현재 과일 종류가 2개를 초과하면 윈도우 축소
    while len(dic) > 2:
        removed = queue.popleft()
        dic[removed] -= 1
        if dic[removed] == 0:
            del dic[removed]
    
    max_length = max(max_length, len(queue))

# 결과 출력
print(max_length)