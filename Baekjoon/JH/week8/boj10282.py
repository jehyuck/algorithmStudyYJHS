import sys
from collections import defaultdict as dd
from collections import deque as ddd

# input = sys.stdin.readline
T = int(input())
INF = 1000000001

for _ in range(T):
    n, d, c = map(int, input().split())
    adj = dd(dict)

    for _ in range(d):
        a, b, s = map(int, input().split())
        # adj[a][b] = s
        adj[b][a] = s

    dp = [INF for _ in range(n+1)]
    dp[0] = dp[c] = 0
    # print(adj[2][1])
    # print(c)
    que = ddd([(c, 0)])
    while que:
        crt_node, crt_dist = que.popleft()

        for next_node in adj[crt_node].keys():
            temp = crt_dist + adj[crt_node][next_node]
            # print(next_node)
            if dp[next_node] > temp:
                dp[next_node] = temp
                que.append((next_node, temp))

    answer_count = 0
    answer_dist = 0
    # print(dp)
    # print(adj)
    for i in range(1, n + 1):
        if dp[i] == INF: continue

        answer_count += 1
        if answer_dist < dp[i]:
            answer_dist = dp[i]

    print(answer_count, answer_dist)
