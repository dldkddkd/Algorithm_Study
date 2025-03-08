def getMaxMoney(money):
    n = len(money)
    if n == 1:
        return money[0]

    dp = [0] * n
    dp[0] = money[0]
    dp[1] = max(money[0], money[1])

    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + money[i])

    return dp[-1]

def solution(money):
    if len(money) == 3:  
        return max(money)

    money1 = getMaxMoney(money[:-1])
    money2 = getMaxMoney(money[1:])

    return max(money1, money2)