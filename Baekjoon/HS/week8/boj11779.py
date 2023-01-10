import sys
from collections import deque
from collections import defaultdict
import heapq


# 다익스트라
def dijkstra():
    pq = []
    # D[i]: 출발점에서 i도시까지 이동하는데 드는 최소 비용
    D = [float('inf') for _ in range(N + 1)]
    # D[i]: i도시까지 최소 비용으로 온 이전 지점
    P = [0] * (N + 1)
    # 시작점에서 시작점까지 최소 비용 = 0
    pq.append((0, start))
    D[start] = 0

    while pq:
        # 현재 도시까지 이동하는데 드는 최소 비용과 도시번호
        cost, city = heapq.heappop(pq)

        # D에서 현재 도시까지의 최소비용 보다 큐에서 나온 도시의 최소비용이 큰 경우
        if D[city] < cost:
            continue

        # 현재 도시가 도착점인 경우
        if city == end:
            break

        for next_cost, next_city in graph[city]:
            # D에서 다음 도시까지 이동하는 최소비용 보다 작은 경우 (최소비용 갱신이 필요한 경우)
            if D[next_city] > D[city] + next_cost:
                # 갱신
                D[next_city] = D[city] + next_cost
                # 다음 도시에 이전 도시 저장
                P[next_city] = city
                # 우선순위큐에 삽입
                heapq.heappush(pq, (D[next_city], next_city))

    # 최소비용, 경로 반환
    return D[end], find_path(P)


# 경로를 찾는 함수
def find_path(P):
    # 경로
    path = deque()
    # 도착점 삽입
    path.appendleft(end)
    # 현재 위치 = 도착점
    cur = end
    # 현재 위치가 출발점이 아닌 경우 반복
    while cur != start:
        # 이전 위치로 이동
        cur = P[cur]
        # 이동한 위치 삽입
        path.appendleft(cur)
    # 경로 반환
    return path


input = sys.stdin.readline

# 도시의 개수
N = int(input())
# 버스의 개수
M = int(input())
# 버스 노선 (그래프)
graph = defaultdict(list)
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

# 출발점, 도착점
start, end = map(int, input().split())

# 최소 비용, 이동 경로
min_cost, path = dijkstra()

print(min_cost)
print(len(path))
print(*path)



