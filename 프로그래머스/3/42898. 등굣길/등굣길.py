def solution(m, n, puddles):
    dp = [[0] * n for _ in range(m)]
    
    dp[0][0] = 1
    
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            
            if [i + 1, j + 1] in puddles:
                dp[i][j] = 0
            else:
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]

    return dp[-1][-1] % 1000000007



