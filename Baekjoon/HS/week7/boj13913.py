import sys
from collections import deque


# BFS 탐색
def bfs():
    q = deque()

    # 수빈이 시작 위치
    q.append(N)
    D[N] = -1

    while q:
        # 수빈이 현재 위치
        X = q.popleft()

        # 수빈이 -1 이동 > 동생을 만나는 경우
        if check(X, X - 1, q):
            # 이동 경로 찾기
            return find_path(X - 1)
        # 수빈이 +1 이동 > 동생을 만나는 경우
        if check(X, X + 1, q):
            # 이동 경로 찾기
            return find_path(X + 1)
        # 수빈이 순간이동 > 동생을 만나는 경우
        if check(X, 2 * X, q):
            # 이동 경로 찾기
            return find_path(2 * X)


# 수빈이 이동 > 동생을 만나는지 확인
def check(cur: int, next: int, q: deque) -> bool:
    # 범위 안이고 이동 위치를 방문한 적이 없는 경우
    if 0 <= next <= 100_000 and D[next] == -9:
        # 수빈이 이동 위치 추가
        q.append(next)
        # D[수빈이 이동 위치] = 현재위치
        D[next] = cur
        # 이동 위치에서 동생을 만나는 경우
        if next == K:
            return True
    return False


# 수빈이 이동 경로 찾기
def find_path(start: int):
    # 이동 경로
    path = deque()

    # 동생 만난 위치 추가
    path.appendleft(start)
    # 동생 만나기 전 위치
    prev = D[start]
    # 동생을 찾는데 걸린 시간
    time = 0

    while prev != -1:
        # 현재 위치 추가
        path.appendleft(prev)
        # 이전 위치
        prev = D[prev]
        # 동생을 찾는데 걸린 시간 증가
        time += 1

    # 동생을 찾는데 걸린 시간과 경로 반환
    return time, path


input = sys.stdin.readline

# 수빈이 위치, 동생 위치
N, K = map(int, input().split())
# 초기화
D = [-9] * 100_001
# 동생 찾는데 걸린 시간
time = 0
# 이동 경로
path = [N]

# 수빈이 위치와 동생 위치가 다른 경우
if N != K:
    # BFS 탐색을 통해 동생을 찾는데 걸린 시간과 이동 경로 찾기
    time, path = bfs()

# 정답 출력
print(time)
print(*path)

