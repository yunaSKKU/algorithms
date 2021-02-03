##<DP - 1. making of the number 1>, from the book <이것이 코딩테스트다>, 217pg
##<DP - 2. tiles>, from the book <이것이 코딩테스트다>,223pg
def one():
    x=int(input())
    dp=[0]*30001 #upper inclusive limit of 30000
    
    for i in range(2,x+1):
        dp[i]=dp[i-1]+1 
        if i%2==0:
            dp[i]=min(dp[i],dp[i//2]+1)
        if i%3==0:
            dp[i]=min(dp[i],dp[i//3]+1)
        if i%5==0:
            dp[i]=min(dp[i],dp[i//5]+1)
    
    return dp[x]
    
def two():
    n=int(input())
    dp=[0]*1001 #upper inclusive limit of 1000
    
    dp[1], dp[2] = 1, 3
    for i in range(3,n+1):
        dp[i]=(dp[i-1]+2*dp[i-2])%796796
    return dp[n]

print(one())
print(two())
