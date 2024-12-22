import sys

N,M = map(int, sys.stdin.readline().split())

pokemon_dict = {}
pokemon_idx ={}

for i in range(N):
  pokemon = sys.stdin.readline().strip()
  pokemon_dict[pokemon] = i+1
  pokemon_idx[i+1] = pokemon
  
for x in range(M):
  prob = sys.stdin.readline().strip()
  if prob.isdigit():
    print(pokemon_idx[int(prob)])
  else:
    print(pokemon_dict[prob])