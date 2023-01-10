import sys
from collections import defaultdict as d
# input = sys.stdin.readline

# 입력값 V, V+1, adj, visit 초기화
V = int(input())
v = V+1

# 노드가 1부터 시작하기에 V+1만큼 초기화
adj = [dict() for _ in range(v)]
visit = [False] * (v)


# adjlist를 입력 받는다 양뱡향으로
for _ in range(V):
    inputs = list(map(int, input().split()))
    n = inputs[0]
    for i in range(1, len(inputs)-1, 2):
        # print(len(inputs), i)
        a = inputs[i]
        b = inputs[i+1]
        adj[n][a] = b
        adj[a][n] = b

# print(*adj)

answer = 0


# dfs를 사용할 것이고, answer = 0으로 초기화
def dfs(node, dist): # node는 현재 위치 dist는 이전 노드에서 전해준 가장 먼 값
    global answer

    # 들어오면 방문처리
    visit[node] = True


    # 현재 노드에서 도달한 곳의 가장 큰값과 두번째로 큰 값만 저장한다.
    no1 = 0
    no2 = 0

    # 이제 갈 수 있는곳을 전부 방문
    for i in adj[node].keys():

        # 이미 방문했다면 가지 않아
        if visit[i]: continue
        # dfs를 통해 방문한 한 노드의 거리가 긴 자식노드를 받는다.
        # 그 값과 그 값 까지 가는데 걸리는 거리를 더한값을 temp에 저장
        temp = dfs(i, adj[node][i] + dist) + adj[node][i]

        # temp 값을 이전에 구한 값과 알맞게 정렬하는
        # 그래서 자식들 중 가장 큰 값2개를 솎아내는 과정
        if temp > no1:
            no2 = no1
            no1 = temp
        elif temp > no2:
            no2 = temp

    # 자식만으로 답을 구해본다
    if answer < no1 + no2:
        answer = no1 + no2

    # 내가 왔던 거리 + 자식놈중 가장큰 값으로 답을 구해본다.
    if answer < dist + no1:
        answer = dist + no1

    # 반환하는 것은 내가 간 것들 중 가장 긴 것
    return no1

# 첫 노드부터 시작을 하고 답을 구해낸다.
dfs(1, 0)
print(answer)