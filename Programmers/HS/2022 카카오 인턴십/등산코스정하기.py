from collections import defaultdict
import heapq

INF = int(1e9)


def solution(n, paths, gates, summits):
    # 양방향 그래프
    graph = defaultdict(list)

    for u, v, w in paths:
        graph[u].append((w, v))
        graph[v].append((w, u))

    # intensity가 최소가 되는 등산코스 찾기
    answer = find_course(n, graph, gates, summits)

    return answer


def find_course(n, graph, gates, summits):
    # intentsity가 최소가 되는 등산코스 (산봉우리, intensity)
    course = [0, INF]
    # 각 지점 까지 이동하는 코스의 최소 intensity
    intensity = dijkstra(n, graph, gates, set(summits))
    # 산봉우리 정렬
    summits.sort()

    # 산봉우리 까지 이동하는 등산코스
    for summit in summits:
        # 기존 등산코스 보다 intensity가 작은 경우
        if course[1] > intensity[summit]:
            # 등산코스 갱신
            course = [summit, intensity[summit]]

    # 등산코스 반환
    return course


def dijkstra(n, graph, gates, summits):
    # 우선순위큐
    pq = []
    # 각 지점까지 이동하는 코스의 최소 intensity
    intensity = [INF] * (n + 1)

    # 출입구
    for gate in gates:
        # 우선순위큐에 삽입
        heapq.heappush(pq, (0, gate))
        # 출입구 intensity = 0
        intensity[gate] = 0

    while pq:
        # 출발 지점까지 intensity, 출발 지점
        from_w, from_v = heapq.heappop(pq)

        # 출발 지점까지 intensity가 최소 intensity 보다 큰 경우
        if intensity[from_v] < from_w:
            continue

        # 도착 지점까지 휴식 없이 이동해야 하는 시간, 도착 지점
        for to_w, to_v in graph[from_v]:
            # 도착 지점까지 intensity
            to_intensity = max(intensity[from_v], to_w)

            # 도착 지점까지 intensity가 최소 intensity 보다 작은 경우
            if intensity[to_v] > to_intensity:
                # 최소 intensity 갱신
                intensity[to_v] = to_intensity

                # 도착 지점이 산봉우리인 경우
                if to_v in summits:
                    continue

                # 우선순위큐에 삽입
                heapq.heappush(pq, (to_intensity, to_v))

    # 각 지점까지 이동하는 코스의 최소 intensity
    return intensity


# 입출력
n = 6
paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
gates = [1, 3]
summits = [5]
result = [5, 3]

print(result == solution(n, paths, gates, summits))