
def fib(n, memo):
    if n in memo: return memo[n]
    if n <= 2: return 1
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    print(f"memo({n}={memo[n]})")
    return memo[n]

def fibonacci(n):
    memo = {}
    val = fib(n, memo)
    return val

print("fib(17)", fibonacci(17))