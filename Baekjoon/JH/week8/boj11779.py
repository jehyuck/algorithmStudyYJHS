import sys
import heapq
from collections import deque
from collections import defaultdict as dd

# input = sys.stdin.readline

N = int(input())# 도시의 갯수
B = int(input())# 버스의 갯수
INF = 100000001

# 버스의 개수가 많으니 인접 리스트?
adj = dd(list)
# 인접리스트 입력받기
for _ in range(B):
    a, b, c, = map(int, input().split())
    adj[a].append((b, c))

# 시작점과 목적지 입력
start, target = map(int, input().split())

# dp를 (최소비용, 이전마을)로 초기화 한다.
dp = [0]
dp.extend([[INF, -1] for i in range(1, N+1)])
dp[start] = [0, -1]
que = [(0, start)]

# 힙큐 다익스트라를 이용한 최소비용 구하기
while que:
    d, node = heapq.heappop(que)

    # 현재 거리가 dp에 기록된 거리보다 커버리면 진행하지 않는다.
    if dp[node][0] < d:
        continue

    # 현재 집이 유망하다면 다음 도시로 전파한다.
    for next_ in range(len(adj[node])):
        nextNode, nextD = adj[node][next_]

        # 유망함을 체크
        temp = nextD + d
        if temp < dp[nextNode][0]:
            dp[nextNode][0] = temp
            dp[nextNode][1] = node
            heapq.heappush(que, (temp, nextNode))

# 역추적을 하면서 도착지점 까지 간다.
answerCount = 0
answerList = deque()
crt = target

while dp[crt][1] != -1:
    answerCount += 1
    answerList.appendleft(crt)
    crt = dp[crt][1]
answerList.appendleft(start)

print(dp[target][0], answerCount + 1, sep='\n')
print(*answerList, sep=' ')