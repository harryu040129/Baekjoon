from collections import deque
import sys

queue = deque()

n = int(sys.stdin.readline().strip())

for i in range(n):
    a, target_index = map(int, sys.stdin.readline().split())
    li = list(map(int, sys.stdin.readline().split()))
    
    queue.clear()
    for idx, x in enumerate(li):
        queue.append((x, idx))  

    cnt = 0

    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:  
            cnt += 1  
            if queue[0][1] == target_index:
                print(cnt)
                break
            else:
                queue.popleft()  
        else:
            queue.rotate(-1)