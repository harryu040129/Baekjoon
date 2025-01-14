import heapq
import sys
from collections import defaultdict

input = sys.stdin.readline # 원래 안쓰는데.. 일단 코드 간결하게 하자

num = int(input())

for _ in range(num):
  n = int(input()) 

  min_heap = []  # 최소 힙 (최솟값을 빠르게 가져오기 위함)
  max_heap = []  # 최대 힙 (최댓값을 빠르게 가져오기 위해 음수로 저장)
  entry_count = defaultdict(int)  # 기본값을 제공하여 존재하지 않는 키에 접근해도 key error가 줄어 확인하는 코드가 줄어든다.

  for _ in range(n):
    command, value = input().strip().split()  # 명령어와 값 입력
    value = int(value)

    if command == 'I':  # 삽입 연산
      heapq.heappush(min_heap, value)  
      heapq.heappush(max_heap, -value) 
      entry_count[value] += 1  # 삽입된 값의 개수를 기록
    elif command == 'D':  # 삭제 연산
      if value == 1:  # 최댓값 삭제
        while max_heap and entry_count[-max_heap[0]] == 0:
          heapq.heappop(max_heap)  # 이미 삭제된 값은 제거 (min에서 생긴 연산)
        if max_heap:  # 유효한 최댓값이 있다면
          max_val = -heapq.heappop(max_heap)
          entry_count[max_val] -= 1 
      elif value == -1:  # 최솟값 삭제
        while min_heap and entry_count[min_heap[0]] == 0:
          heapq.heappop(min_heap)  # 이미 삭제된 값은 제거 (max에서 생긴 연산)
        if min_heap:  # 유효한 최솟값이 있다면
          min_val = heapq.heappop(min_heap) 
          entry_count[min_val] -= 1 

  # 모든 연산 후 유효하지 않은 값 정리 (위랑 동일한 logic)
  while min_heap and entry_count[min_heap[0]] == 0:
    heapq.heappop(min_heap) 
  while max_heap and entry_count[-max_heap[0]] == 0:
    heapq.heappop(max_heap) 

  # 결과 출력
  if min_heap and max_heap:  
    print(-max_heap[0], min_heap[0])
  else: 
    print("EMPTY")