import sys
import heapq as h
from collections import deque as d

# input = sys.stdin.readline

N = int(input()) #타일의 갯수
NN = N*N-N//2
dr = (-1, 0, 1, -1, 0, 1)
dcE = (-1, -1, -1, 0, 1, 0)
dcO = (0, -1, 0, 1, 1, 1)


def check_bound(r, c, o):
    cc = N if o % 2 == 0 else N - 1
    if 0 <= r < N and 0 <= c < cc: return True
    return False

board = []

# 타일의 입력
idx = 1
for i in range(N):
    temp = []
    for _ in range(N if i % 2 == 0 else N - 1):
        a, b = map(int, input().split())
        temp.append((a, b, idx))
        idx += 1
    board.append(temp)
# print(*board, sep='\n')


dist = 1      # 정답
answer = 0
answer_count = 0
answer_node = [0, 0]
visit = [0] + [[-1, -1, -1] for _ in range(NN)]     # 방문 좌표
que = d([(0, 0)])     # bfs사용을 위한 큐

while que:
    dist += 1
    size = len(que)
    temp = d()

    for i in range(size):
        r, c = que.popleft()

        dc = dcE if r % 2 == 0 else dcO

        for j in range(3):
            nr = r + dr[j]
            nc = c + dc[j]
            if check_bound(nr, nc, nr):
                n = board[nr][nc][2]
            else:
                continue
            # print(nr, nc, n)
            # print(check_bound(nr, nc, r) , board[r][c][0] == board[nr][nc][1] , visit[n][0] == -1)
            if board[r][c][0] == board[nr][nc][1] and visit[n][0] == -1:
                visit[n][0] = r
                visit[n][1] = c
                visit[n][2] = dist
                if answer < n:
                    answer_node = [nr, nc]
                    answer_count = dist
                    answer = n
                temp.append((nr, nc))

        for j in range(3, 6):
            nr = r + dr[j]
            nc = c + dc[j]
            if check_bound(nr, nc, nr):
                n = board[nr][nc][2]
            else:
                continue
            # print(nr, nc, n)
            # print(check_bound(nr, nc, nr) , board[r][c][1] == board[nr][nc][0] , visit[n][0] == -1)
            if board[r][c][1] == board[nr][nc][0] and visit[n][2] == -1:
                visit[n][0] = r
                visit[n][1] = c
                visit[n][2] = dist
                if answer < n:
                    answer_node = [nr, nc]
                    answer_count = dist
                    answer = n
                temp.append((nr, nc))
    que = temp

r, c = answer_node
answer_que = d([board[r][c][2]])
print(answer_count)

while answer_count > 1:
    answer_count -= 1
    r, c, _ = visit[board[r][c][2]]
    answer_que.appendleft(board[r][c][2])
print(*answer_que)
# while answer_find_que:
#     r, c = answer_find_que
# print(answer, answer_node)
# print(visit)
