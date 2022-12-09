import sys
from collections import deque as d
# input = sys.stdin.readline

N, M = map(int, input().split())
n = N - 1
m = M - 1

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

board=[list(map(int, list(input()))) for _ in range(N)]
answer=[board[i].copy() for i in range(N)]
visit=[[False] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] == 0 and not visit[i][j]:
            visit[i][j] = True
            visitSet = set()
            que = d()
            que.append((i, j))
            visitCount = 0
            # print(i, j)
            # print(i, j, end='->')
            while que:
                cr, cc = que.popleft()
                visitCount += 1
                # print((cr, cc), end=' ')
                for d_ in range(4):
                    nr = cr + dr[d_]
                    nc = cc + dc[d_]

                    if 0 > nr or nr > n or 0 > nc or nc > m: continue
                    if visit[nr][nc] : continue
                    if board[nr][nc] != 0:
                        visitSet.add((nr, nc))
                        continue

                    visit[nr][nc] = True
                    que.append((nr, nc))
            # print('\n', visitCount)
            for r, c in visitSet:
                answer[r][c] = (answer[r][c] + visitCount) % 10

for i in range(N):
    print(*answer[i], sep='')


# print(*board, sep='\n')