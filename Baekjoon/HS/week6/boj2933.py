import sys
from collections import deque

input = sys.stdin.readline

# 동굴의 크기 R, C
R, C = map(int, input().split())
# 동굴 (미네랄: x, 빈공간: .)
cave = [list(input().rstrip()) for _ in range(R)]
# 막대를 던진 횟수
N = int(input())
# 막대를 던진 높이
heights = list(map(int, input().split()))

# 좌, 우, 상, 하
d = [(0, -1), (0, 1), (-1, 0), (1, 0)]


# 막대 던지기
def throw_stick(turn: int, height: int):
    # 홀수면 1, 짝수면 0
    is_odd = turn % 2
    # 막대를 던지는 초기 위치
    x, y = R - height, 0 if is_odd else C - 1
    # 막대를 던지는 방향
    dx, dy = d[is_odd]

    while cave[x][y] == '.':
        x, y = x + dx, y + dy
        # 범위를 벗어난 경우 -> 부술 미네랄이 없음
        if not in_range(x, y):
            return

    # 미넬랄 부수기
    break_mineral(x, y)


# 미네랄 부수기
def break_mineral(x, y):
    # 미넬랄 부수기
    cave[x][y] = '.'
    # 방문 체크를 위한 배열
    visited = [[0] * C for _ in range(R)]

    # 4방 탐색
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        # 범위 밖이거나 미네랄이 없거나 방문했던 위치인 경우
        if not in_range(nx, ny) or cave[nx][ny] == '.' or visited[nx][ny]:
            continue
        # 미네랄 클러스터
        cluster = []
        # 클러스터가 떠있는 경우
        if is_floating(nx, ny, cluster, visited):
            # 클러스터 떨어뜨리기
            fall_cluster(cluster)
            return


# 클러스터가 떠있는지 확인
def is_floating(x, y, cluster, visited):
    # 떠있다.
    floating = True
    # BFS 탐색을 위한 큐
    q = deque([(x, y)])
    # 방문 체크
    visited[x][y] = 1
    # 클러스터 속한 미네랄 추가
    cluster.append((x, y))
    while q:
        x, y = q.popleft()

        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if not in_range(nx, ny) or cave[nx][ny] == '.' or visited[nx][ny]:
                # 바닥에 닿은 경우 -> 떠있지 않음.
                if nx == R:
                    floating = False
                continue
            q.append((nx, ny))
            visited[nx][ny] = 1
            cluster.append((nx, ny))

    return floating


# 클러스터 떨어뜨리기
def fall_cluster(cluster: list):
    for x, y in cluster:
        # 미네랄 지우기
        cave[x][y] = '.'

    finish = False

    # 클러스터 미네랄을 하나씩 떨어뜨리기
    while True:
        new_cluster = []
        for x, y in cluster:
            nx = x + 1
            if not in_range(nx, y) or cave[nx][y] != '.':
                finish = True
                break
            new_cluster.append((nx, y))

        if finish:
            break;

        cluster = new_cluster

    # 클러스터 떨어진 위치에 미네랄 표시
    for x, y in cluster:
        cave[x][y] = 'x'


# 동굴 범위 확인
def in_range(x, y):
    if 0 <= x < R and 0 <= y < C:
        return True
    return False


# 동굴 미네랄 모양 출력
def print_cave():
    for row in cave:
        print(*row, sep='')


for i, h in enumerate(heights, start=1):
    throw_stick(i, h)

print_cave()
