import sys

input = sys.stdin.readline

INF = int(1e9)

V, E = map(int, input().split())

adj = [[INF] * V for _ in range(V)]

for i in range(V):
    adj[i][i] = 0

for _ in range(E):
    a, b, c = map(int, input().split())
    adj[a-1][b-1] = c

# 플로이드-워셜
for k in range(V):
    for i in range(V):
        for j in range(V):
            if adj[i][k] + adj[k][j] < adj[i][j]:
                adj[i][j] = adj[i][k] + adj[k][j]

answer = INF

for i in range(V):
    for j in range(i + 1, V):
        answer = min(answer, adj[i][j] + adj[j][i])

print(answer if answer != INF else -1)