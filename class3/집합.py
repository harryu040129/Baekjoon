"""비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다.
"""

import sys

def add(s,x):
  s.add(x)

def remove(s,x):
  s.discard(x)

def check(s,x):
  if x in s:
    print(1)
  else:
    print(0)

def toggle(s,x):
  if x in s:
    s.remove(x)
  else:
    s.add(x)

def all(s):
  s.clear()
  s.update(range(1,21))

def empty(s):
  s.clear()

num_i = int(sys.stdin.readline())
s = set()
for i in range(num_i):
  oper = list(sys.stdin.readline().split())
  if len(oper) == 2:
    locals()[oper[0]](s,int(oper[1]))
  elif len(oper) == 1:
    locals()[oper[0]](s)
