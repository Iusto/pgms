def solution(n):
    # 1,2,3,5 이거보고 피보나치수 바로 생각남
    answer = 0
    dp = [0] * (n+1)
    
    dp[0] = 1
    dp[1] = 1
    
    # dp를 통해 중복되는 계산 수를 줄임
    
    for i in range(2, n+1):
        dp[i] = (dp[i-2] + dp[i-1]) % 1000000007
    
    return dp[n]