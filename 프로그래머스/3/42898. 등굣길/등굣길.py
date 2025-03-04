def solution(m, n, puddles):
    MOD = 1000000007
    dp = [0] * (m + 1)
    dp[1] = 1
    
    puddle_set = {(y, x) for x, y in puddles}
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (i, j) == (1, 1):
                continue
            if (i, j) in puddle_set:
                dp[j] = 0
            else:
                dp[j] = (dp[j] + dp[j - 1]) % MOD
    
    return dp[m]