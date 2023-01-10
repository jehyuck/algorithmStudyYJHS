import sys
from collections import defaultdict
import heapq


def dijkstra():
    pq = []

    heapq.heappush(pq, (0, c))
    D[c] = 0

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)

        if D[cur_node] < cur_cost:
            continue

        for next_cost, next_node in graph[cur_node]:
            if D[next_node] > D[cur_node] + next_cost:
                D[next_node] = D[cur_node] + next_cost
                heapq.heappush(pq, (D[next_node], next_node))


def check():
    count = 0
    time = 0

    for t in D:
        if t == INF:
            continue

        count += 1
        time = max(time, t)

    return count, time


sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

INF = int(1e9)

T = int(input())

for _ in range(T):
    n, d, c = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((s, a))
    D = [INF] * (n + 1)

    dijkstra()
    answer = check()
    print(*answer)
