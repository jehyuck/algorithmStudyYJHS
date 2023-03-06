from collections import deque as d
from collections import defaultdict as dd


def solution(info, edges):
    answer = 0
    graph = dd(list)

    # 트리로 그래프를 만든다. 양방향 그래프
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    for i in range(len(info)):
        if info[i] == 0:
            visit = [False] * len(info)
            que = d()
            que.append(i)
            answer = max(answer, get_answer(i, que, visit, info, graph, 0, 0))

    # print(graph)
    return answer


# 리턴 값은 양의 수
# 답을 구하기 위한 재귀 함수
# 이 재귀에서 구하고있는 count가 0이 되면 안된다, 재귀를 들어오기 전에 미리 계산한다.
def get_answer(crt, que, visit, info, graph, sheep, wolf):
    # que에 현재 내가 방문할 수 있는 곳을 전부 집어넣는다.
    rtn = 0
    temp = d()
    # print(crt)
    while que:
        node = que.pop()
        # 방문한 곳이면 아무런 처리도 안한다.
        if visit[node]:
            continue
        # 늑대면 후보로 두고
        if info[node] == 1:
            temp.append(node)
        # 양이면 방문하고 값을 처리한다.
        else:
            # print("여기오나", node)
            visit[node] = True
            rtn += 1
            sheep += 1
            for put in graph[node]:
                if visit[put]:
                    continue
                if info[put] == 0:
                    que.append(put)
                else:
                    temp.append(put)

    que = temp
    # 늑대면 갈지 말지 고민한다.
    # print("sheep-wolf: ", sheep-wolf)
    if sheep - wolf <= 1:
        return rtn
    max_count = 0

    # print(que)
    # print("--------------------------")
    for node in que:
        visit[node] = True
        new_que = que.copy()
        new_que.extend(graph[node])
        max_count = max(max_count, get_answer(node, new_que, visit.copy(), info, graph, sheep, wolf + 1))
    return rtn + max_count
