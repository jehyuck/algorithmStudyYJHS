import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

INF = int(1e9)

T = int(input())

# 테스트케이스 수 만큼 반복
for _ in range(T):
    N, M, K = map(int, input().split())

    # 그래프 (인접 리스트)
    graph = defaultdict(list)

    for _ in range(K):
        u, v, c, d = map(int, input().split())
        graph[u].append((d, c, v))

    # dp[i][j] = 1번 공항에서 i번 공항까지 j(비용)로 가는 최단거리
    dp = [[INF] * (M + 1) for _ in range(N + 1)]
    # 우선순위큐 (거리, 비용, 공항)
    pq = [(0, 0, 1)]

    while pq:
        # 거리, 비용, 공항
        d, c, v = heapq.heappop(pq)

        # d가 1번 공항에서 v번 공항까지 c(비용)로 가는 최단 거리 보다 큰 경우
        if d > dp[v][c]:
            continue

        for nd, nc, nv in graph[v]:
            # v와 인접한 nv 까지 가는데 필요한 비용과 거리
            cost = c + nc
            distance = d + nd

            # 최대 비용 보다 큰 경우
            if cost > M:
                continue

            # 최단 거리 보다 작은 경우
            if distance < dp[nv][cost]:
                # 최단 거리 갱신
                for i in range(cost, M + 1):
                    if distance < dp[nv][i]:
                        dp[nv][i] = distance
                    else:
                        break
                # 우선순위큐에 삽입
                heapq.heappush(pq, (distance, cost, nv))

    # 정답
    answer = dp[N][M]
    print(answer if answer != INF else 'Poor KCM')

