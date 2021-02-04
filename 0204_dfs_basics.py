#dfs 1. How many ice cream bars could you make from the ice mold?
#from the book <이것이 코딩 테스트다> 149pg

def dfs(i,j):
    if i<=-1 or i>=n or j<=-1 or j>=m:
        return False
    if given[i][j]==0:
        given[i][j]=1
        dfs(i-1,j)
        dfs(i+1,j)
        dfs(i,j-1)
        dfs(i,j+1)
        return True
    return False

n,m=map(int,input().split())
given=[]
for i in range(n):
    given.append(list(map(int,input())))

count=0
for a in range(n):
    for b in range(m):
        if dfs(a,b)==True:
            count+=1
print(count)
