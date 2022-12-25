import sys
from collections import deque


def bfs():
    q = deque()
    visited = [[0] * C for _ in range(R)]

    # 타일 단위로 큐에 넣기 (타일 하나 = 조각 두개)
    q.append((0, 0))
    q.append((0, 1))
    # 방문 체크
    visited[0][0] = visited[0][1] = 1

    # 이동 가능한 가장 큰 타일 번호
    max_num = 1
    # 이동 가능한 가장 큰 타일 번호의 위치
    mx, my = 0, 0

    while q:
        x, y = q.popleft()

        for dx, dy in d:
            # 인접한 위치
            nx1, ny1 = x + dx, y + dy

            # 범위 확인
            if not (0 <= nx1 < R and 0 <= ny1 < C):
                continue
            # 인접한 조각과 다른 숫자가 적힌 경우 또는 이미 방문한 경우
            if tiles[x][y] != tiles[nx1][ny1] or visited[nx1][ny1]:
                continue

            # 같은 타일의 다른 조각 위치
            nx2, ny2 = same_tile(nx1, ny1)
            # 타일의 두 조각 위치 큐에 삽입
            q.append((nx1, ny1))
            q.append((nx2, ny2))
            # 방문 체크
            visited[nx1][ny1] = visited[nx2][ny2] = visited[x][y] + 1
            # 인접한 타일의 타일 번호
            next_num = tile_nums[nx1][ny1]

            # 인접한 타일의 타일 번호가 마지막 타일의 번호인 경우
            if next_num == end_num:
                # 마지막 타일로 이동하는 경로 찾기
                return find_path(nx1, ny1, visited);

            # 인접한 타일의 타일 번호가 최대 타일 번호 보다 큰 경우
            if max_num < next_num:
                # 최대번호와 위치 갱신
                max_num = next_num
                mx, my = nx1, ny1

    # 가장 큰 타일로 이동하는 경로 찾기
    return find_path(mx, my, visited)


# 경로 찾기
def find_path(x1, y1, visited):
    path = deque()
    cnt = visited[x1][y1]
    x2, y2 = same_tile(x1, y1)

    for i in range(cnt, 0, -1):
        tile_num = tile_nums[x1][y1]
        # 타일 번호를 왼쪽에 삽입
        path.appendleft(tile_num)

        for dx, dy in d:
            nx1, ny1 = x1 + dx, y1 + dy
            # 첫번재 조각으로 경로 확인
            if check_path(x1, y1, nx1, ny1, i - 1, visited):
                x1, y1 = nx1, ny1
                x2, y2 = same_tile(x1, y1)
                break

            nx2, ny2 = x2 + dx, y2 + dy
            # 두번째 조각으로 경로 확인
            if check_path(x2, y2, nx2, ny2, i - 1, visited):
                x1, y1 = nx2, ny2
                x2, y2 = same_tile(x1, y1)
                break
    # 경로 반환
    return path


# 경로 확인
def check_path(x, y, nx, ny, cnt, visited):
    # 범위 밖인 경우 또는 경로의 길이가 다른 경우
    if not (0 <= nx < R and 0 <= ny < C) or visited[nx][ny] != cnt:
        return False
    # 인접한 타일 조각에 적힌 숫자가 다른 경우
    if tiles[x][y] != tiles[nx][ny]:
        return False

    return True


# 같은 타일의 다른 조각의 위치 반환
def same_tile(x, y):
    # 왼쪽의 조각이 같은 타일인 경우
    if 0 <= y - 1 and tile_nums[x][y] == tile_nums[x][y - 1]:
        return x, y - 1
    # 오른쪽의 조각이 같은 타일인 경우
    return x, y + 1


input = sys.stdin.readline

d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

N = int(input())
R, C = N, 2 * N
# 타일 조각에 적힌 숫자
tiles = [[0] * C for _ in range(R)]
# 타일의 번호
tile_nums = [[0] * C for _ in range(R)]
# 마지막 타일의 번호
end_num = 0
for i in range(R):
    start = 0
    # 짝수 줄인 경우
    if i % 2:
        # 한칸 띄우고 시작
        start = 1
    for j in range(start, C - 1, 2):
        end_num += 1
        # 타일 조각에 숫자 적기
        tiles[i][j], tiles[i][j + 1] = map(int, input().split())
        # 타일의 번호
        tile_nums[i][j] = tile_nums[i][j + 1] = end_num

path = bfs()

print(len(path))
print(*path)
