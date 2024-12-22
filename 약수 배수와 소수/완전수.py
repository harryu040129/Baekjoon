def perfectNum(n):
  fac = []
  sum = 0
  for i in range(n//2):
    if n%(i+1) == 0:
      fac.append(i+1)
      sum += i+1
  if sum == n:
    perfectPrinter(n, fac, True)
  else:
    perfectPrinter(n, fac, False)
  
def perfectPrinter(n, li, bo):
  if bo:
    print("{} = ".format(n), end = "")
    for x in li:
      print("{}".format(x), end = "")
      if x != li[-1]:
        print(" + ", end = "")
    print()
  else:
    print("{} is NOT perfect.".format(n))

while True:
  n = int(input())
  if n == -1:
    break
  perfectNum(n)
