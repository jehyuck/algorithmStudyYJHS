import sys

input = sys.stdin.readline

N = 8
board = [list(input().rstrip()) for _ in range(N)]
d = [(0, 0), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def solution():
    # 초기 욱제 위치 (집합)
    wook = {(N - 1, 0)}

    # 초기 벽 위치
    wall = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == '#':
                wall.append((i, j))

    # 벽이 없어질 때까지 반복
    while wall:
        # 1초 뒤 욱제와 벽 위치
        new_wook = set()
        new_wall = []

        for x, y in wall:
            # 범위를 벗어난 경우
            if x + 1 >= N:
                continue
            # 1초 뒤 벽 위치 추가
            new_wall.append((x + 1, y))

        for x, y in wook:
            for dx, dy in d:
                nx, ny = x + dx, y + dy

                # 범위를 벗어난 경우
                if not (0 <= nx < N and 0 <= ny < N):
                    continue

                # 욱제가 이동할 위치에 현재 벽이 있거나 1초 뒤 벽이 있는 경우
                if (nx, ny) in wall or (nx, ny) in new_wall:
                    continue

                # 욱제가 이동할 수 있는 위치 추가 (중복 방지 위해 집합 사용)
                new_wook.add((nx, ny))

        # 욱제와 벽 위치 갱신
        wook = new_wook
        wall = new_wall

    # 욱제가 이동할 수 있는 위치가 있는 경우 1, 없는 경우 0
    return 1 if wook else 0


answer = solution()
print(answer)

