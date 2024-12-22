n = int(input())
# 1 2 3
# 1 4 16 ...
# 4 9 25 ...
n = 4**n
n = n**0.5
n += 1
n = n**2
print(int(n))