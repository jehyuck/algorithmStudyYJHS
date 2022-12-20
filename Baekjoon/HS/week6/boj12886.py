import sys
from collections import deque


def solution(stones):
    # 돌의 개수 총합
    total = sum(stones)
    # 총합이 3으로 나누어 떨어지지 않는 경우
    if total % 3:
        return 0

    # 돌의 개수 정렬
    stones.sort()
    # 작은값, 중간값, 큰값
    A, B, C = stones

    # 모두 같으면 1
    if A == B == C:
        return 1

    # 큐
    q = deque()
    # 방문 체크 -> [중간값][큰값 - 작은값]
    visited = [[0] * 1501 for _ in range(1501)]

    # 정렬된 돌 그룹 삽입
    q.append(stones)
    # 중간값, 큰값 - 작은값
    visited[B][C - A] = 1

    while q:
        stones = q.popleft()

        # 이동시킬 첫번째 돌 그룹
        for i in range(2):
            # 이동시킬 두번째 돌 그룹
            for j in range(i + 1, 3):
                # 이동시키지 않는 돌 그룹
                k = 3 - i - j
                X, Y, Z = stones[i], stones[j], stones[k]
                # 이동시키려는 두개의 돌 그룹의 돌 개수가 서로 같은 경우
                if X == Y:
                    continue
                # 돌 이동
                new_stones = [X + X, Y - X, Z]
                # 정렬
                new_stones.sort()
                # 작은값, 중간값, 큰값
                nA, nB, nC = new_stones

                # 세 돌 그룹의 돌 개수가 같으 경우
                if nA == nB == nC:
                    return 1
                # 이미 선택했던 조합인 경우
                if visited[nB][nC - nA]:
                    continue
                # 돌 그룹 삽입
                q.append(new_stones)
                # 방문 체크 -> [중간값][큰값 - 작은값]
                visited[nB][nC - nA] = 1

    return 0


input = sys.stdin.readline

stones = list(map(int, input().split()))

answer = solution(stones)
print(answer)

