import sys

input = sys.stdin.readline

N = int(input())
home = [list(input().rstrip()) for _ in range(N)]

# 문 위치 저장
doors = []
# 한 쪽 문에서 출발해서 각 좌표까지 이동하는데 필요한 최소 거울 수
visited = [[-1] * N for _ in range(N)]
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for i in range(N):
    for j in range(N):
        if home[i][j] == '#':
            doors.append((i, j))


def solution():
    q = [doors[0]]
    # 거울 수
    count = 0
    visited[doors[0][0]][doors[0][1]] = count
    while q:
        new_q = []
        for x, y in q:
            for dx, dy in d:
                nx, ny = x, y
                # 각 방향으로 빛을 쏠 때
                while True:
                    nx += dx
                    ny += dy

                    # 범위를 벗어나거나, 벽인 경우
                    if not (0 <= nx < N and 0 <= ny < N) or home[nx][ny] == '*':
                        break

                    # 이미 지나간 곳인 경우
                    if visited[nx][ny] != -1:
                        continue

                    # 해당 좌표까지 이동하는데 필요한 최소 거울 수
                    visited[nx][ny] = count

                    # 다른 쪽 문인 경우
                    if home[nx][ny] == '#':
                        return count
                    # 거울인 경우
                    elif home[nx][ny] == '!':
                        new_q.append((nx, ny))
        # 큐 갱신
        q = new_q
        # 거울 수 증가
        count += 1


answer = solution()
print(answer)

