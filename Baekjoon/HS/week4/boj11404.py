import sys

input = sys.stdin.readline

INF = int(1e9)

n = int(input())
m = int(input())

adj = [[INF] * n for _ in range(n)]

for i in range(n):
    adj[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a-1][b-1] = min(adj[a-1][b-1], c)

# 플로이드-워셜
for k in range(n):
    for i in range(n):
        for j in range(n):
            if adj[i][k] + adj[k][j] < adj[i][j]:
                adj[i][j] = adj[i][k] + adj[k][j]

for i in range(n):
    for j in range(n):
        if adj[i][j] == INF:
            adj[i][j] = 0

for row in adj:
    print(*row)