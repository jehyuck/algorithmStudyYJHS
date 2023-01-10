import sys
from collections import deque


def is_in(x: int, y: int):
    if 0 <= x <= N and 0 <= y <= M:
        return True
    return False


def solution(A1, A2, B1, B2):
    visited_A = [[-1] * (M + 1) for _ in range(N + 1)]
    visited_B = [[-1] * (M + 1) for _ in range(N + 1)]

    visited_A[B1[0]][B1[1]] = -9
    visited_A[B2[0]][B2[1]] = -9
    visited_B[A1[0]][A1[1]] = -9
    visited_B[A2[0]][A2[1]] = -9

    answer = 0

    q = deque()

    q.append(A1)
    visited_A[A1[0]][A1[1]] = 0

    while q:
        current = q.popleft()
        x, y = current

        for dx, dy in d:
            nx, ny = x + dx, y + dy

            if not is_in(nx, ny):
                continue

            if visited_A[nx][ny] != -1:
                continue

            q.append((nx, ny))
            visited_A[nx][ny] = visited_A[x][y] + 1

    if visited_A[A2[0]][A2[1]] < 0:
        return INF

    answer += visited_A[A2[0]][A2[1]]

    q.append(A2)
    visited_B[A2[0]][A2[1]] = -9

    while q:
        current = q.popleft()
        x, y = current

        if visited_A[x][y] == 0:
            break

        for dx, dy in d:
            nx, ny = x + dx, y + dy

            if not is_in(nx, ny):
                continue

            if visited_A[x][y] == visited_A[nx][ny] + 1:
                q.append((nx, ny))
                visited_B[nx][ny] = -9
                break

    q.append(B1)
    visited_B[B1[0]][B1[1]] = 0

    while q:
        current = q.popleft()
        x, y = current

        for dx, dy in d:
            nx, ny = x + dx, y + dy

            if not is_in(nx, ny):
                continue

            if visited_B[nx][ny] != -1:
                continue

            q.append((nx, ny))
            visited_B[nx][ny] = visited_B[x][y] + 1

    if visited_B[B2[0]][B2[1]] < 0:
        return INF

    answer += visited_B[B2[0]][B2[1]]

    return answer


sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

INF = int(1e9)
d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

N, M = map(int, input().split())
A1 = tuple(map(int, input().split()))
A2 = tuple(map(int, input().split()))
B1 = tuple(map(int, input().split()))
B2 = tuple(map(int, input().split()))

answer = min(solution(A1, A2, B1, B2), solution(B1, B2, A1, A2))

print(answer if answer != INF else "IMPOSSIBLE")


