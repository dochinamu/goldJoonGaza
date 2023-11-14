def factorial(n):
    num = 1
    for i in range(1, 1+n):
       num *= i
    return num 
    
t = int(input())
for _ in range(t):
    n,m = list(map(int, input().split()))
    print(factorial(m) // (factorial(m-n) * factorial(n)))
    


   

# import sys

# t = int(sys.stdin.readline())
# dp = [[0]*30 for _ in range(30)]

# for i in range(30):
#     for j in range(30):
#         if i == 1:
#             dp[i][j] = j
#         else:
#             if i == j:
#                 dp[i][j] = 1
#             elif i < j:
#                 dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

# for i in range(t):
#     n, m = map(int, sys.stdin.readline().split())
#     print(dp[n][m])