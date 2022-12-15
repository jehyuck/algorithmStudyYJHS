import sys
from collections import deque


# 선으로 이어진 부분을 지우는 함수
def bfs(x, y):
    q = deque()
    # 큐에 삽입
    q.append((x, y))
    # 선 지우기
    plain[x][y] = 0

    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            # 범위 밖인 경우
            if not (0 <= nx < 2001 and 0 <= ny < 2001):
                continue
            # 선이 없는 경우
            if not plain[nx][ny]:
                continue
            # 큐에 삽입
            q.append((nx, ny))
            # 선 지우기
            plain[nx][ny] = 0


input = sys.stdin.readline

# 상 하 좌 우
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# 직사각형의 개수
N = int(input())
# 좌표 평면 (-1000 <= 2 * x1 < 2 * x2 <= 1000), (-1000 <= 2 * y1 < 2 * y2 <= 1000)
plain = [[0] * 2001 for _ in range(2001)]
# PU 명령의 최솟값
count = 0

for _ in range(N):
    # 직사각형의 좌표 x1, y1, x2, y2
    coordinate = list(map(int, input().split()))
    for i in range(4):
        # 직사각형의 좌표 변화 -> 2 * x + 1000
        coordinate[i] = 2 * coordinate[i] + 1000
    x1, y1, x2, y2 = coordinate
    # 직사각형 그리기
    for i in range(x1, x2 + 1):
        plain[i][y1] = 1
        plain[i][y2] = 1
    for j in range(y1, y2 + 1):
        plain[x1][j] = 1
        plain[x2][j] = 1

# (0, 0)에서 PD상태로 시작하므로 (0, 0)에 직사각형의 일부일 경우 -1 부터 시작
if plain[1000][1000]:
    count -= 1

# 전체 좌표 평면 탐색
for i in range(2001):
    for j in range(2001):
        # (i, j)에 직사각형이 그려져 있는 경우
        if plain[i][j]:
            # 연결되어 있는 선을 전부 지우기
            bfs(i, j)
            # 카운트 증가
            count += 1

# 정답 출력
print(count)
