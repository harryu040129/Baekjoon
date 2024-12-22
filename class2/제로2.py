import sys

n = int(sys.stdin.readline()) 

if n == 0: 
    print(0)
    sys.exit()

stack = [0] * n 

num = int(n * 0.15 + 0.5)


for i in range(n):
    inp = int(sys.stdin.readline())
    stack[i] = inp

def mergeSort(A, p, r):
    if p < r:
        mid = (p + r) // 2
        mergeSort(A, p, mid) 
        mergeSort(A, mid + 1, r) 
        merge(A, p, mid, r)

def merge(A, p, mid, r):
    n1 = mid - p + 1
    n2 = r - mid
    
    li1 = [0] * (n1)
    li2 = [0] * (n2)

    for i in range(n1):
        li1[i] = A[p + i]
    for j in range(n2):
        li2[j] = A[mid + 1 + j]
    
    li1.append(float("inf"))
    li2.append(float("inf"))
    
    i = 0
    j = 0
    for k in range(p, r + 1):
        if li1[i] <= li2[j]:
            A[k] = li1[i]
            i += 1
        else:
            A[k] = li2[j]
            j += 1

mergeSort(stack, 0, n - 1)

if n != 0: 
  print(round(sum(stack[num:n-num])/(n-2*num)))
else:
    print(0)  