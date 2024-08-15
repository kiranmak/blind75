def sum_possible(amount, numbers):
    return sum_possible_dp(amount, numbers, memo={})

def sum_possible_dp(amount, numbers, memo):
    if amount in memo: return memo[amount]
    if amount == 0: return True
    if amount < 0: return False

    for num in numbers:
        remaining = amount - num
        if sum_possible_dp(remaining, numbers, memo):
            memo[amount] = True # beause + num it is possible
            return True
    memo[amount] = False
    return False
    
# Run test for sum_possible
ans = sum_possible(8, [5, 12, 4]) # -> True, 4 + 4
print("ans for 8, [5, 12, 4] ", ans)

sum_possible(15, [6, 2, 10, 19]) # -> False
print("sum_possible(15, [6, 2, 10, 19]", ans)

ans = sum_possible(103, [6, 20, 1]) # -> True
print("sum_possible(103, [6, 20, 1])", ans) # -> True
sum_possible(271, [10, 8, 265, 24]) # -> False
print("sum_possible(271, [10, 8, 265, 24])", ans)