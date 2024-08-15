import sys
def min_change(amount, coins):
    #ans = min_change_brute(amount, coins)
    ans = min_change_dp(amount, coins, memo={})
    return ans 

def min_change_brute(amount, coins):
    if amount < 0: return -1
    if amount == 0: return 0
    
    min_coins = sys.maxsize
    
    for coin in coins:
        left = amount - coin
        count = min_change(left, coins)
        if count < 0:
            continue
        count += 1
        if count < min_coins: 
            min_coins = count

    if min_coins == sys.maxsize:
        min_coins = -1
    return min_coins
            
def min_change_dp(amount, coins, memo):
    if amount in memo: return memo[amount]
    if amount == 0: return 0
    if amount < 0: return -1
    
    min_coins = sys.maxsize
    
    for coin in coins:
        left = amount - coin
        count = min_change_dp(left, coins, memo)
        if count == -1:
            memo[amount] = count 
            continue
        if count < min_coins: 
            min_coins = count + 1

    if min_coins == sys.maxsize:
        min_coins = -1
    memo[amount] = min_coins
    return min_coins

ans = min_change(8, [1, 5, 4, 12]) # -> 2,
print("min_change(8, [1, 5, 4, 12]) ", ans)
'''
ans = min_change(13, [1, 9, 5, 14, 30]) # -> 5
print("min_change(13, [1, 9, 5, 14, 30]) # -> 5/", ans)

ans = min_change(2017, [4, 2, 10]) # -> -1
print("min_change(2017, [4, 2, 10]) # -> -1/", ans)
'''