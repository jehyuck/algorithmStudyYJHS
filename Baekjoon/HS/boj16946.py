import sys


def bfs(x, y):
    q = [(x, y)]
    arr[x][y] = -1
    # 해당 영역의 크기
    count = 1
    # 해당 영역과 인접한 벽
    edges = set()

    while q:
        new_q = []

        for x, y in q:
            for dx, dy in d:
                nx, ny = x + dx, y + dy

                # 범위 확인
                if not (0 <= nx < N and 0 <= ny < M):
                    continue
                # 벽인 경우
                if arr[nx][ny] == 1:
                    edges.add((nx, ny))
                    continue
                # 방문한 경우
                if arr[nx][ny] == -1:
                    continue

                new_q.append((nx, ny))
                arr[nx][ny] = -1
                count += 1

        q = new_q

    # 인접한 벽들의 위치에 해당 영역의 크기 추가
    for x, y in edges:
        answer[x][y] = (answer[x][y] + count) % 10


input = sys.stdin.readline

N, M = map(int, input().split())

# 방문체크할 2차원 배열
arr = [list(map(int, input().rstrip())) for _ in range(N)]
# 정답을 저장할 2차원 배열
answer = [row.copy() for row in arr]

d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for i in range(N):
    for j in range(M):
        if arr[i][j] != 0:
            continue
        bfs(i, j)

for row in answer:
    print(*row, sep='')



