N,k = map(int,input().split())
li = list(map(int,input().split()))

li = sorted(li)[::-1]

print(li[k-1])