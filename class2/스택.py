import sys

class stack:
  def __init__(self):
    self.stack = []
  
  def push(self, element):
    self.stack.append(element)
  
  def pop(self):
    if self.stack:
      temp = self.stack.pop()
      print(temp)
    else:
      print(-1)
  
  def top(self):
    if self.stack:
      print(self.stack[-1])
      return
    print(-1)

  def empty(self):
    if not self.stack:
      print(1)
    else:
      print(0)
  
  def size(self):
    print(len(self.stack))



n = int(sys.stdin.readline())

sta = stack()

for i in range(n):
  ord = list(sys.stdin.readline().split())
  command = ord[0]
  if len(ord) == 2:
    getattr(sta,command)(int(ord[1]))
  else:
    getattr(sta,command)()
