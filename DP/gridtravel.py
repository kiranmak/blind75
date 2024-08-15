
def gridTraveler_dp(m, n, memo):
    key = str(m) + "," + str(n)
    if key in memo: return memo[key]
    if m == 1 and n == 1: return 1
    if m == 0 or n == 0: return 0
    result = gridTraveler_dp(m -1, n, memo) + gridTraveler_dp(m, n-1, memo)
    memo[key] = result
    return result

def gridTraveler(m, n):
    table = [[0] * (n+1) for _ in range(m+1)]
    table[1][1] = 1

    for i in range(m+1): 
        for j in range(n+1): 
            curr = table[i][j]
            if (j+1) <= n:
                table[i][j + 1] += curr
            if (i+1) <= m:
                table[i + 1][j] += curr

    return table[m][n]
    
print("gridTraveler(2,3) 3/", gridTraveler(2,3))
print("gridTraveler(18,18) 3/", gridTraveler(18,18))
#print("gridTraveler(3,3) 6/", gridTraveler(3,3))

#print("gridTraveler(3,3)6/", gridTraveler(3,3, memo={}))
#print("gridTraveler(13,13)", gridTraveler(13,13, memo={}))
    