import sys
from collections import deque as dd

# input = sys.stdin.readline

R, C = map(int, input().split()) # board의 크기
board = [list(input()) for _ in range(R)] # board 입력
N = int(input()) # 던진 횟수 입력
sticks = tuple(map(int, input().split())) # 던진 막대의 높이
# visit을 던질 때마다 초기화
visit = [[[False for _ in range(C)] for _ in range(R)] for _ in range(N)]

ch = 0          # 왼쪽에서 던질경우 C
s = C - 1       # 오른쪽 C
floor = R - 1   # 바닥 index(Row)

# 방향 배열
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)


# 클러스터를 찾아 분리하고 떨어트리는 동작이 담긴 함수
def find_cluster(r, c, n):# r, c 각 각 시작 행 열
    # 클러스터 후보를 찾는다
    hubo = []

    for j in range(4):
        nr = r + dr[j]
        nc = c + dc[j]
        # 범위 밖이면 체크를 안한다.
        if check_bound(nr, nc): continue
        if board[nr][nc] == 'x': hubo.append(dd([(nr, nc)]))

    # print(hubo)
    # 후보가 한개면 더 확인 안해도 된다.
    # if len(hubo) == 1: return

    # 후보가 여러개면 분리된 클러스터를 찾아내야 한다.
    # 하나 하나를 visit하면서 bfs로 뭉치를 찾아낸다(저장하면서 찾음).
    # 높이도 기록해야 바닥에 붙어 있는지 안다.
    # 분리된 클러스터가 단 한개라고 나와있기 떄문에 한개를 찾으면 그만
    # print(hubo)
    for j in range(len(hubo)):
        que = hubo.pop() # 후보중 한개를 뽑음
        if visit[n][que[0][0]][que[0][1]]: continue
        crt_floor = que[0][0] # 후보의 높이
        visit[n][que[0][0]][que[0][1]] = True # 후보 현재 위치를 ture
        cluster = dd() # 후보의 클러스터 조합을 담을 그릇

        # print(que, crt_floor, floor)
        # 큐의 클러스터 뭉치를 찾는다.
        while que:
            cr, cc = que.popleft()

            for q in range(4): # 4 방향에 대해
                fnr = cr + dr[q]
                fnc = cc + dc[q]

                # 범위 체크 방문체크
                if check_bound(fnr, fnc): continue
                if visit[n][fnr][fnc] or board[fnr][fnc] == '.': continue

                # 범위 안에 있으면 방문, que 에 넣어준다. 높이비교를 해 바닥인지 체크
                crt_floor = max(crt_floor, fnr)
                visit[n][fnr][fnc] = True

                # print(fnr, fnc, )
                que.append((fnr, fnc))

            cluster.append([cr, cc])

        # 바닥에 도달한 클러스터면 밑으로 내리는 작업을 하지 않아도 됨
        if crt_floor == floor: continue
        # print(cluster, crt_floor, floor)
        # 바닥이 아니면
        # 지도에서 클러스터를 지워주고 한칸씩 내려가며 다른 벽을 만날 때 까지
        for k in cluster:
            cl_r, cl_c = k
            board[cl_r][cl_c] = '.'

        # 혹은 바닥에 갈 때까지 한칸씩 내린다.
        go_floor = True
        # print("cluster..........",cluster)
        while go_floor and crt_floor != floor:
            crt_floor += 1

            # 클러스터 요소를 순회
            for k in cluster:
                k[0] += 1
                cl_r, cl_c = k # 클러스터 요소들 한개를 행 열 뽑아냄
                # print(k, go_floor)
                # 바뀐 위치에서 주변에 닿는게 있는지 확인
                if go_floor:
                    for q in range(2):
                        fnr = cl_r + dr[q]
                        fnc = cl_c + dc[q]

                        # 범위체크
                        # print(board[nr][nc])
                        if check_bound(fnr, fnc): continue
                        # 주변에 닿으면 플래그를 바꿔준다.
                        if board[fnr][fnc] == 'x': go_floor = False
        # print("move cluster................", cluster)
        # 전부 내렸으면 다시 칠해준다.
        for k in cluster:
            cl_r, cl_c = k
            board[cl_r][cl_c] = 'x'
        # print("moved board................")
        # print(*board, sep='\n')
        break


# 밖을 나갔냐 안나걌냐를 체크해 주는 함수
def check_bound(r, c):
    if 0 <= r < R and 0 <= c < C: return False
    return True


# 막대를 전부 던지기 위한 반복문
for i in range(N):
    # print(i)
    # print(*board,sep='\n')

    # i가 짝수면 왼쪽에서 던짐
    d, cStart = [1, ch] if i % 2 == 0 else [-1, s] # 사람 과 증감값 설정
    rStart = R - sticks[i] # 시작 행

    # 던지면 위치를 찾아준다.
    find = False
    while 0 <= cStart < C:
        if board[rStart][cStart] == 'x':
            find = True
            break
        cStart += d
    # print("removed.........",rStart, cStart, d)

    # 던진 위치를 찾으면면 빈 간으로 만들어 주고
    if find:
        board[rStart][cStart] = '.'
        # print(*board,sep='\n')
        # 클러스터 움직이는 작업을 시작한다.
        find_cluster(rStart, cStart, i)

# 정답을 출력
for i in board:
    print(''.join(i))

