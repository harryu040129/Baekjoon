import sys

def MergeSort(arr, s_index, e_index):
  if s_index < e_index:
    mid = (s_index+e_index)//2
    MergeSort(arr,s_index,mid)
    MergeSort(arr,mid+1,e_index)
    Merge(arr, s_index, mid, e_index)
  
def Merge(arr, s_index, mid, e_index):
  size1 = mid-s_index+1
  size2 = e_index-mid
  l = [0] * (size1)
  r = [0] * (size2)
  for i in range(size1):
    l[i] = arr[s_index+i]
  for j in range(size2):
    r[j] = arr[mid+j+1]
  l.append(float('inf'))
  r.append(float('inf'))
  i,j = 0,0
  for k in range(s_index,e_index+1):
    if l[i] <= r[j]:
      arr[k] = l[i]
      i+=1
    else:
      arr[k] = r[j]
      j+=1

def binarySearch(arr,x,s_index,e_index):
  if s_index>e_index:
    return 0
  mid = (s_index+e_index)//2
  if arr[mid] == x:
    return 1
  elif arr[mid]>x:
    return binarySearch(arr,x,s_index,mid-1)
  elif arr[mid]<x:
    return binarySearch(arr,x,mid+1,e_index)

N = int(sys.stdin.readline())
lin = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
lim = list(map(int,sys.stdin.readline().split()))

MergeSort(lin,0,N-1)

for i in range(M):
  print(binarySearch(lin,lim[i],0,N-1))

