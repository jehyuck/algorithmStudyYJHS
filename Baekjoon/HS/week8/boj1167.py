import sys
from collections import defaultdict

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# 트리의 정점의 개수
V = int(input())
# 트리 -> 그래프
graph = defaultdict(list)

for _ in range(V):
    # 입력
    line = list(map(int, input().split()))
    # 정점 번호
    u = line[0]
    idx = 1
    while line[idx] != -1:
        # 연결된 정점 번화, 거리
        v, w = line[idx], line[idx + 1]
        graph[u].append((v, w))
        idx += 2

# 정답 > 트리의 지름
answer = 0
# 방문 확인
visited = [0] * (V + 1)


# 탐색하는 함수 (현재 노드, 이전 노드와 현재 노드 사이 거리, 시작 노드부터 현재 노드까지 거리)
def search(current: int, prev_weight: int, total: int):
    # 트리의 지름
    global answer

    # 현재 노드 방문 체크
    visited[current] = 1

    first = total
    second = 0

    max_ = 0

    for next, weight in graph[current]:
        if visited[next]:
            continue

        cost = search(next, weight, total + weight)

        max_ = max(max_, cost)

        if first < cost:
            first, second = cost, first
        elif second < cost:
            second = cost

    answer = max(answer, first + second)

    return max_ + prev_weight


search(1, 0, 0)

print(answer)