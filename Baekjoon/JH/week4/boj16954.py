from collections import deque as d
board = [list(input()) for _ in range(8)]

dr = (0, 0, -1, -1, -1, 0, 1, 1, 1)
dc = (-1, 1, -1, 0, 1, 0, -1, 0, 1)

start = (7, 0)

wall = d()

for i in range(8):
    for j in range(8):
        if board[i][j] == '#':
            wall.append([i, j])
# print(wall)
que = d()
que.append(start)
for _ in range(8):
    size = len(que)
    while size > 0:
        size -= 1
        cr, cc = que.popleft()
        if board[cr][cc] == '#':
            continue
        board[cr][cc] = '.'
        # print(cr, cc, end='-> ')
        for i in range(9):
            nr = cr + dr[i]
            nc = cc + dc[i]

            if 0 > nr or 0 > nc or 8 <= nr or 8 <= nc: continue
            if board[nr][nc] != '.': continue
            # print((nr, nc, board[nr][nc]), end=' ')
            board[nr][nc] = '!'
            que.append((nr, nc))
        # print()
    size = len(wall)
    while size > 0:
        size -= 1
        cr, cc = wall.pop()
        board[cr][cc] = '.'
        # print(cr, cc)
        nr = cr + 1

        if 0 > nr or 0 > nc or 8 <= nr or 8 <= nc: continue
        board[nr][cc] = '#'
        wall.appendleft((nr, cc))
    # print("stage start...................")
    # print(*board, sep="\n")
print(0 if 0 == len(que) else 1)
