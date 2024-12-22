li = []

for i in range(5):
  li.append(int(input()))

li = sorted(li)

print(int(sum(li)/5))
print(li[2])