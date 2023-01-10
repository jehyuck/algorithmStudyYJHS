import sys
from collections import deque


def bfs(x: int, y: int, horse: str):
    q = deque()

    q.append((x, y))
    visited[x][y] = 1

    success = False

    while q:
        x, y = q.popleft()

        for dx, dy in d:

            one_line = True

            for k in range(1, 3):
                nx, ny = x + k * dx, y + k * dy

                if not in_range(nx, ny) or board[nx][ny] != horse:
                    one_line = False
                    break

                if not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1

            if one_line:
                success = True

    if success:
        return True

    return False


def in_range(x: int, y: int) -> bool:
    if 0 <= x < ROW_SIZE and 0 <= y < COL_SIZE:
        return True
    return False


def check():
    if X_cnt == O_cnt + 1 and X_success and not O_success:
        return True
    elif X_cnt == O_cnt and O_success and not X_success:
        return True
    elif X_cnt == O_cnt + 1 and X_cnt + O_cnt == SIZE and not X_success and not O_success:
        return True
    return False


sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

ROW_SIZE = 3
COL_SIZE = 3
SIZE = ROW_SIZE * COL_SIZE

d = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

while True:
    line = input().rstrip()

    if line == "end":
        break

    board = [list(line[i:i+COL_SIZE]) for i in range(0, SIZE, ROW_SIZE)]
    visited = [[0] * COL_SIZE for _ in range(ROW_SIZE)]

    X_cnt = 0
    O_cnt = 0

    X_success = False
    O_success = False

    for i in range(ROW_SIZE):
        for j in range(COL_SIZE):
            if board[i][j] == 'X':
                X_cnt += 1
                if not X_success and not visited[i][j]:
                    X_success = bfs(i, j, 'X')
            elif board[i][j] == 'O':
                O_cnt += 1
                if not O_success and not visited[i][j]:
                    O_success = bfs(i, j, 'O')

    print("valid" if check() else "invalid")





