import sys

def Merge(arr, s_index, m_index, e_index):
  size1 = m_index-s_index+1 # calculate size of the first sublist
  size2 = e_index - m_index # calculate the size of the second sublist
  L = [] # left sublist
  R = [] # right sublist
  for i in range(size1):
    L.append(arr[s_index+i]) # finish creating left sublist
  for j in range(size2):
    R.append(arr[m_index+j+1]) # finish creating right sublist
  L.append(float('inf')) # create sentinel
  R.append(float('inf'))
  i,j = 0,0 # create two index variable
  for k in range(s_index, e_index+1): # loop to create merged array from start index to end index
    if L[i] <= R[j]: # compare left and right sublist and append greater value
        arr[k] = L[i]
        i += 1 # adjust indexes according to the sublist the element appended from
    else:
        arr[k] = R[j]
        j += 1
# Function to split the arrays by means of merge sort algorithm and perform merge as well
# Time complexity:  O(n \log n) 
def MergeSort(arr, s_index, e_index):
    if s_index < e_index: # while start index is less than end index
        mid_index = (s_index+e_index) // 2 # find mid index
        MergeSort(arr, s_index, mid_index) # split the left sublist into binary tree shape
        MergeSort(arr, mid_index + 1, e_index) # split the right sublist into binary tree shape
        Merge(arr, s_index, mid_index, e_index) # merge all the sublists created from above process

N = int(sys.stdin.readline())
li = []

for i in range(N):
  li.append(int(input()))

MergeSort(li, 0, len(li)-1)

for i in range(N):
  print(li[i])