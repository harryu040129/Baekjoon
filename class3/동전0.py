"""
import sys

N, K = map(int, sys.stdin.readline().split())

comb = []
for x in range(N):
  coin = int(sys.stdin.readline().strip())
  if coin > K:
    continue
  else:
    comb.append(coin)

comb.sort(reverse=True) 
count = 0

for coin in comb:
    if K == 0:
        break
    count += K // coin  
    K = K - coin * (K // coin)       

print(count)
"""
import sys

N, K = map(int, sys.stdin.readline().split())

coins = []
for _ in range(N):
    coin = int(sys.stdin.readline().strip())
    if coin <= K:  # Only add coins that are less than or equal to K
        coins.append(coin)

def bruteforce(target, idx, count):
    # Base cases
    if target == 0:  # Found a valid combination
        return count
    if target < 0 or idx >= len(coins):  # Invalid combination
        return float('inf')
    
    # Try two options for each coin:
    # 1. Use the current coin
    # 2. Skip the current coin
    use_coin = bruteforce(target - coins[idx], idx, count + 1)
    skip_coin = bruteforce(target, idx + 1, count)
    
    return min(use_coin, skip_coin)

result = bruteforce(K, 0, 0)
print(result)