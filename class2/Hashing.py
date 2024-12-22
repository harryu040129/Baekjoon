import sys

n = int(sys.stdin.readline())
code = sys.stdin.readline()

res = 0

for i in range(n):
  res += (ord(code[i])-96) * (31**i) # ord 를 넣어서 아스키코드를 따오는데 알파벳을 표현하려면 96을 빼줘야함

print(res%1234567891)