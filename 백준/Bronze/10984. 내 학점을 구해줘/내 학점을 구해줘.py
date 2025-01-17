import sys

T = int(sys.stdin.readline())

for _ in range(T):
  N = int(sys.stdin.readline())
  n_cnt, gpa_avg = 0, 0
  for i in range(N):
    a,b = map(float, sys.stdin.readline().strip().split())

    n_cnt += a
    gpa_avg += b*a
  gpa_avg /= n_cnt
  print(f'{int(n_cnt)} {gpa_avg:.1f}')