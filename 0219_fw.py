INF = int(1e9)
n,m=map(int,input().split())
graph=[[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    if a==b:
        graph[a][b]=0
    else:
        graph[a][b]=1
        graph[b][a]=1

X,K=map(int,input().split())

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

our_answer=graph[1][K] + graph[K][X]

if our_answer>=INF:
    print("-1")
else:
    print(our_answer)

