import sys

# input = sys.stdin.readline

V, E = map(int, input().split())
INF = 80000000
adj = [[INF] * (V+1) for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    adj[a][b] = c
    # adj[b][a] = c

for k in range(V+1):
    for i in range(V+1):
        # if i==k: continue
        for j in range(V+1):
            # if i == j: continue
            temp = adj[i][k] + adj[k][j]
            if temp < adj[i][j]:
                adj[i][j] = temp

answer = INF
for i in range(1, V+1):
    answer = min(answer, adj[i][i])
print(answer if answer != INF else -1, sep="\n")

# for i in range(V):
#     for j in range(V):
#         if i==j: continue
#         temp = adj[i][j] + adj[j][i]
#         print(i, j, temp, adj[i][i])
#         if adj[i][j] + adj[j][i] < adj[i][i]:
#             adj[i][i] = temp



