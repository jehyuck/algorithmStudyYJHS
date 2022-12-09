import sys
from collections import deque as d_
# input = sys.stdin.readline
T = int(input())
INF = 100001


#비용이 낮고 빠른거 1
#똑같은 경로에 대해 조작해야 하는 경우
# 1 5, 2 4, 3 3, 4 2, 5 1

for _ in range(T):
    # 단방향 그래프
    # 공항수 N, 노드
    # 총지원비용 M, 제약
    # 티켓 정보의 수 K, 간선 수
    N, M, K = map(int, input().split())
    n = N+1
    m = M+1

    #인접 행렬 사용해 보기
    adj = [[]  for _ in range(n)]
    dist = [[INF] * m for _ in range(n)]
    dist[1][0] = 0
    #간선의 수 만큼 입력 받기
    for i in range(K):
        # 시간 정렬 기준
        u, v, c, d = map(int, input().split())
        adj[u].append((v,c,d))

    que = d_()
    que.append((1, 0, 0)) #도시 비용 시간

    while que:
        v, c, d = que.popleft()

        if d > dist[v][c]:
            continue

        for i in range(len(adj[v])):
            nNode, nc, nd = adj[v][i]

            nCost = nc + c
            nTime = nd + d
            if nCost <= M and nTime < dist[nNode][nCost]:
                for j in range(nCost, m):
                    if nTime < dist[nNode][j]:
                        dist[nNode][j] = nTime
                    else:
                        break
                que.append((nNode, nCost, nTime))

    # print(*dist, sep='\n')
    ans = dist[N][M]
    print(ans if ans != INF else "Poor KCM")