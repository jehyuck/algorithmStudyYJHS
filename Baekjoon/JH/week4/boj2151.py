import sys
import heapq as h
# from collections import deque as d

# input = sys.stdin.readline


n = int(input())

dr = (-1, 0, 1, 0)
dc = (0, -1, 0, 1)

board = [list(input()) for _ in range(n)]
visit = [[[2500, 2500, 2500, 2500] for _ in range(n)] for _ in range(n)]
start = 0

for i in range(n):
    for j in range(n):
        if board[i][j] == '#':
            start = (i, j)
            board[i][j] = '.'
            break
    if type(start) == tuple:
        break


def check(r, c, board, start):
    if 0 > r or 0 > c or n <= r or n <= c : return False
    if board[r][c] == '*': return False
    return True


que = []
sr, sc = start
# que.append((0, 0, start))
# que.append((0, 1, start))
# que.append((0, 2, start))
# que.append((0, 3, start))
h.heappush(que, (0, 0, (sr, sc, True)))
h.heappush(que, (0, 1, (sr, sc, True)))
h.heappush(que, (0, 2, (sr, sc, True)))
h.heappush(que, (0, 3, (sr, sc, True)))
answer = 2501
while que:
    # print(*visit, sep="\n")
    dist, d, p = h.heappop(que)
    # print(dist, d, p)
    cr, cc, go = p

    visit[cr][cc][d] = dist
    if board[cr][cc] == '#':
        # print(dist, p)
        answer = min(answer, dist)
        continue
    nr = cr + dr[d]
    nc = cc + dc[d]
    # print(nr, nc)

    if not check(nr, nc, board, start): continue
    if visit[nr][nc][d] <= dist: continue

    if board[nr][nc] == '!':
        h.heappush(que, (dist, d, (nr, nc, True)))
        # print(lr, lc, l, dist, visit[lr][lc][l])
        l = (d + 1) % 4
        r = (d + 3) % 4
        if check(nr, nc, board, start) and visit[nr][nc][l] > dist + 1:
            # que.append((dist + 1, l, (lr, lc)))
            h.heappush(que, (dist + 1, l, (nr, nc, False)))

        if check(nr, nc, board, start) and visit[nr][nc][r] > dist + 1:
            # print(rr, rc)
            # que.append((dist + 1, r, (rr, rc)))
            h.heappush(que, (dist + 1, r, (nr, nc, False)))
    else:
        h.heappush(que, (dist, d, (nr, nc, True)))
# visit = [[[0] * 4] * n for _ in range(n)]
print(answer)

