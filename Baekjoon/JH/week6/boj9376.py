import sys
import heapq as h
from collections import deque as dd

input = sys.stdin.readline

# 문을 여는 갯수의 최댓값
INF = 100 * 100 + 1
# 방향 변화 값
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# 답을 구하는 함수
def find_solution():
    r, c = map(int, input().split()) # map의 행, 열을 입력
    R = r + 1
    C = c + 1
    CC = c + 2

    board = [['.']*(c+2)]
    board.extend([['.']+list(input())+['.'] for _ in range(r)]) # 맵의 상태를 입력
    board.append(['.']*(c+2))

    p = [None, None] # 죄수의 좌표를 담을 arr
    idx = 0          # 죄수를 넘버링
    for i in range(1, R):
        for j in range(1, C):
            if board[i][j] == '$':
                p[idx] = (i, j) # 죄수의 좌표를 담는다.
                idx += 1        # 다음 죄수를 찾는다.

    # 다익스트라를 통해 죄수가 나가는 경우의 수를 구한다.
    # r + 2, c + 2만큼의 visit을 만들어준다.
    p1_visit = [[INF] * (C + 1) for _ in range(R + 1)]
    p2_visit = [[INF] * (C + 1) for _ in range(R + 1)]
    zero_visit = [[INF] * (C + 1) for _ in range(R + 1)]
    # 각 위치에서 최소의 문을 여는 갯수를 visit 배열에 저장해 준다
    escape_door_count(R, C, *p[0], p1_visit, board)
    escape_door_count(R, C, *p[1], p2_visit, board)
    escape_door_count(R, C, 0, 0, zero_visit, board)

    # print(*p1_visit,sep='\n')
    # print(*p2_visit,sep='\n')
    # print(*zero_visit, sep='\n')
    # 한 점에서 문을 열때 탈출하려면 드는 값을 구한다.
    # 정답을 도달할 수 없는 최댓값으로 설정
    answer = INF
    if zero_visit[p[0][0]][p[0][1]] == 0 and zero_visit[p[1][0]][p[1][1]] == 0:
        return 0

    # 모든 점에 대해서 그 점에서 도착지, 1번죄수, 2번죄수가 만날 경우에만을 고려하고 그 지점에서 답을 구한다.
    # 그 지점에서 만난다면 죄수1 + 죄수2 + 도착지점, 3가지를 따졌을 때 그 문까지 걸리는 시간을 구하면 된다.
    for i in range(R + 1):
        for j in range(CC):
            if board[i][j] != '#': continue
            # print(p1_visit[i][j] , p2_visit[i][j] , zero_visit[i][j])
            temp = p1_visit[i][j] + p2_visit[i][j] + zero_visit[i][j]
            # print("왜지-->", temp, (i,j))
            answer = min(answer, temp - 2)

    # print(*board, sep='\n')
    return answer


# 죄수가 나가기 위한 다익스트라를 구하는 함수
def escape_door_count(r, c, pr, pc, visit, board):
    que = [(0, pr, pc)]
    visit[pr][pc] = 0

    R = r + 1
    C = c + 1

    # 힙큐를 통해 모든 지점에 대해 최솟값을 구한다.
    while que:
        c_count, cr, cc = h.heappop(que)

        # 방문된 기록중 더 작은게 있다면 하지 않는다.
        if c_count > visit[cr][cc]:
            continue

        # 4방향에 대해서 전파한다.
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]

            # 범위를 나갔으면 아무것도 하지 않는다.
            if check_bound(R, C, nr, nc): continue
            # print("check Bound ------------->??", (nr, nc), (R, C))
            # 각 문자 모양에 대해 다른 처리를 해준다.
            if board[nr][nc] == '*':
                continue
            else:
                n_count = c_count + 1 if board[nr][nc] == '#' else c_count
                if n_count < visit[nr][nc]:
                    visit[nr][nc] = n_count
                    h.heappush(que, (n_count, nr, nc))







# 탈출했냐 안했냐를 반환하는 함수.
def check_escape(r, c, rr, cc):
    if 1 <= rr < r and 1 <= cc < c:
        return False
    return True


# 범위를 벗어나는지 체크
def check_bound(r, c, rr, cc):
    if 0 <= rr < r and 0 <= cc < c:
        return False
    return True


T = int(input())
for _ in range(T):
    print(find_solution())
