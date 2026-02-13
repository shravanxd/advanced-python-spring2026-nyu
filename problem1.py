import time

def f_rec(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return f_rec(n-1) + f_rec(n-2) + f_rec(n-5)

def f_memo_helper(n, memo):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n in memo:
        return memo[n]
    
    res = f_memo_helper(n-1, memo) + f_memo_helper(n-2, memo) + f_memo_helper(n-5, memo)
    memo[n] = res
    return res

def f_memo(n):
    memo = {}
    return f_memo_helper(n, memo)

def f_it(n):
    if n < 0: return 0
    if n == 0: return 1
    
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        if i >= 1:
            dp[i] += dp[i-1]
        if i >= 2:
            dp[i] += dp[i-2]
        if i >= 5:
            dp[i] += dp[i-5]
            
    return dp[n]

def time_function(func, args):
    start = time.time()
    result = func(args)
    end = time.time()
    return end - start

if __name__ == "__main__":
    print("--- Problem 1 Solution ---")
    
    # Validating with examples
    print(f"f(1) = {f_it(1)} (Expected: 1)")
    print(f"f(2) = {f_it(2)} (Expected: 2)")
    print(f"f(3) = {f_it(3)} (Expected: 3)")
    print(f"f(5) = {f_it(5)} (Expected: 9)")
    print()

    # Part 1: Recursive Timing
    print("Recursive Solution Timing:")
    for n in [10, 25]:
        t = time_function(f_rec, n)
        print(f"n={n}: {t:.6f} seconds")
    print()

    # Part 2: Memoized Timing
    print("Memoized Solution Timing:")
    for n in [10, 25, 50, 100]:
        t = time_function(f_memo, n)
        print(f"n={n}: {t:.6f} seconds")
    print()

    # Part 3: Iterative Timing
    print("Iterative Solution Timing:")
    for n in [10, 25, 50, 100]:
        t = time_function(f_it, n)
        print(f"n={n}: {t:.6f} seconds")
