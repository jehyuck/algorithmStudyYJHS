import sys
from collections import deque as d
# input = sys.stdin.readline

N, M = map(int, input().split())
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
dirIdx = {'|':(0, 1), '-':(2, 3),'+': (0, 1, 2, 3),'1':(1, 3),'2':(0, 3),'3':(0,2),'4':(1, 2), 'M': (), 'Z': ()}

board = [list(input()) for _ in range(N)]
visit = [[False] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] == '.':
            board[i][j] = 0

hubo = set()
for i in range(N):
    for j in range(M):
        if board[i][j] in dirIdx and not visit[i][j]:
            visit[i][j] = True
            que = d()
            que.append((i,j))
            while que:
                cr, cc = que.popleft()

                for d_ in dirIdx[board[cr][cc]]:
                    nr = cr + dr[d_]
                    nc = cc + dc[d_]

                    if 0 > nr or nr >= N or 0 > nc or nc >=M: continue
                    if type(board[nr][nc]) == int:
                        # print(nr, nc, d_,"엥")
                        board[nr][nc] += 1 << d_
                        hubo.add((nr,nc))
                        continue
                    if visit[nr][nc]: continue
                    visit[nr][nc] = True
                    que.append((nr, nc))

r, c = hubo.pop()
holls = []
answer = 0
n = 0
for d_ in range(4):
    if board[r][c] & 1<<(d_) != 0:
        # print(n, d_, 1<<d_)
        put = 0
        if d_ == 0:
            put = 1
        elif d_ == 1:
            put = 0
        elif d_ == 2:
            put = 3
        else:
            put = 2
        holls.append(put)

holls_ = tuple(sorted(holls))
# print(holls, board[r][c])
for i in dirIdx.keys():
    # print(holls_, dirIdx[i])
    if dirIdx[i] == holls_:
        answer = i
        break
print(r+1,c+1, answer)
# print(answer)
# print(hubo)