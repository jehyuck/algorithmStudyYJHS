import sys

# input = sys.stdin.readline

INF = 100 * 100000 + 1
N = int(input())
M = int(input())

n = N+1
m = M+1
adj = [[INF] * n for _ in range(n)]

for i in range(M):
    a,b,c = map(int, input().split())

    adj[a][b] = min(adj[a][b], c)

for k in range(1, n):
    for i in range(1, n):
        for j in range(1, n):
            if i==j: continue
            temp = adj[i][k] + adj[k][j]
            if temp < adj[i][j]:
                adj[i][j] = temp
# print(*adj[1:], sep='\n')
for i in range(1, n):
    for j in range(1, n):
        adj[i][j] = 0 if adj[i][j] == INF else adj[i][j]

for i in range(1, n):
    print(*adj[i][1:])