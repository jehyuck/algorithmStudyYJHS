import sys
# input = sys.stdin.readline

N = int(input())
INF = 17000001
allVisit = (1 << N) - 1
adj = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if adj[i][j] == 0:
            adj[i][j] = INF

dp = [[0] * N for _ in range(1 << N)]


# 외판원 순회 문제
def tsp(visit, now):
    global adj, dp, allVisit, INF

    # 현재 위치를 방문한다
    visit |= 1 << now

    # visit가 전체 방문한 경우 출발도시로 돌아간다. 못가면 INF 반환
    if visit == allVisit:
        # print(now ,'--->',bin(visit), allVisit,'-------------')
        if adj[now][0] != INF:
            return adj[now][0]
        return INF

    # 현재 방문한적 있는 노드면은 그 값을 바로 리턴한다.
    if dp[visit][now] != 0:
        return dp[visit][now]

    # 방문한적 없는 상태면 진행
    dp[visit][now] = INF
    # 아니면은 방문 할 수 있는 곳 중에 최선책을 찾아낸다.
    for i in range(N):
        temp = 0
        # 방문 할 수 있으면
        if i != now and visit & (1 << i) == 0 and adj[now][i] != INF:
            # 값을 계산하고
            temp = tsp(visit, i) + adj[now][i]

            # 최선책일 경우 갱신한다.
            if temp < dp[visit][now]:
                # print(now, '->', (i, visit), temp)
                dp[visit][now] = temp

    # 이때 구한 최선책을 return 한다.
    return dp[visit][now]


print(tsp(0, 0))

'''
예외 케이스 왜??
16
0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 0 1 1 1 1 1 1 1 1 1 1 1 1 1
0 1 1 0 1 1 1 1 1 1 1 1 1 1 1 1
0 1 1 1 0 1 1 1 1 1 1 1 1 1 1 1
0 1 1 1 1 0 1 1 1 1 1 1 1 1 1 1
0 1 1 1 1 1 0 1 1 1 1 1 1 1 1 1
0 1 1 1 1 1 1 0 1 1 1 1 1 1 1 1
0 1 1 1 1 1 1 1 0 1 1 1 1 1 1 1
0 1 1 1 1 1 1 1 1 0 1 1 1 1 1 1
0 1 1 1 1 1 1 1 1 1 0 1 1 1 1 1
0 1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
0 1 1 1 1 1 1 1 1 1 1 1 0 1 1 1
0 1 1 1 1 1 1 1 1 1 1 1 1 0 1 1
0 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1
0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0
이유를 모르겠지만 visit 처리를 INF로 안하고 0으로 하니 해결됨

#풀이가 다른것 같은 블로그
https://aigong.tistory.com/568

'''
