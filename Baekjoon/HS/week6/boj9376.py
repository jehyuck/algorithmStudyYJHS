import sys


def solution():
    # 0: 감옥밖, 1: 죄수1, 2: 죄수2
    for i, (x, y) in enumerate(start):
        cnt = 0
        q = [(x, y)]
        D[x][y][i] = cnt

        while q:
            new_q = []
            for x, y in q:
                for dx, dy in d:
                    nx, ny = x + dx, y + dy
                    # 범위 밖인 경우
                    if not (0 <= nx < H + 2 and 0 <= ny < W + 2):
                        continue
                    # 방문한 적이 있거나, 벽인 경우
                    if D[nx][ny][i] != -1 or prison[nx][ny] == '*':
                        continue
                    # 문인 경우 > 현재
                    if prison[nx][ny] == '#':
                        # 새로운 큐에 삽입
                        new_q.append((nx, ny))
                        # 열어야 하는 문의 수 추가
                        D[nx][ny][i] = cnt + 1
                    # 문이 아닌 경우 > 지나갈 수 있음.
                    else:
                        # 현재 큐에 삽입
                        q.append((nx, ny))
                        # 추가로 열어야 하는 문 없음
                        D[nx][ny][i] = cnt

            # 열어야 하는 문의 수 추가
            cnt += 1
            # 큐 갱신
            q = new_q

    return check()


def check():
    q = [(0, 0)]
    visited = [[0] * (W + 2) for _ in range(H + 2)]
    visited[0][0] = 1

    # 두 죄수를 탈옥시키기 위해서 열어야 하는 문의 최솟값
    min_cnt = 0
    for k in range(3):
        min_cnt += D[0][0][k]

    while q:
        new_q = []

        for x, y in q:
            for dx, dy in d:
                nx, ny = x + dx, y + dy
                # 범위 밖인 경우
                if not (0 <= nx < H + 2 and 0 <= ny < W + 2):
                    continue
                # 방문한 적이 있거나, 벽인 경우
                if visited[nx][ny] or prison[nx][ny] == '*':
                    continue
                # 현재 위치를 통해 두 죄수를 탈옥시키기 위해서 열어야 하는 문의 최솟값
                cnt = 0
                for k in range(3):
                    cnt += D[nx][ny][k]
                # 현재 위치가 문인 경우 > 중복으로 카운팅 됨
                if prison[nx][ny] == '#':
                    cnt -= 2

                new_q.append((nx, ny))
                visited[nx][ny] = 1

                # 최소값 갱신
                min_cnt = min(min_cnt, cnt)
        # 큐 갱신
        q = new_q

    # 최소값 반환
    return min_cnt


input = sys.stdin.readline

d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 테스트 케이스의 개수
T = int(input())

for _ in range(T):
    # 평면도의 높이, 너비
    H, W = map(int, input().split())
    # 감옥
    prison = [['.'] * (W + 2) for _ in range(H + 2)]
    # 출발 위치: 감옥 밖, 죄수1, 죄수2
    start = [(0, 0)]
    # D[i][j][k]: k가 i, j 위치까지 이동하기 위해 열어야 하는 문의 최솟값
    D = [[[-1] * 3 for _ in range(W + 2)] for _ in range(H + 2)]

    for i in range(1, H + 1):
        line = list(input().rstrip())
        for j in range(1, W + 1):
            prison[i][j] = line[j - 1]
            if prison[i][j] == '$':
                # 죄수 위치 추가
                start.append((i, j))

    # 두 죄수를 탈옥시키기 위해서 열어야 하는 문의 최솟값
    answer = solution()
    print(answer)




