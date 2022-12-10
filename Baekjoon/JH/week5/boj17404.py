import sys

# input = sys.stdin.readline

#집의 갯수를 입력받음
N = int(input())

#N개의 집을 각 3개의 색으로 칠할 때 들어가는 비용을 배열로 받는다.
colorCost = [list(map(int, input().split())) for _ in range(N)]

#끝에 값을 고정하기 위해서 첫 배열을 0으로 두는 각각의 dp테이블을 만들어 놓는다.
INF = 1000001
dp1 = [colorCost[0].copy()]
dp1[0][0] = INF
dp1.extend(colorCost[1:].copy())

dp2 = [colorCost[0].copy()]
dp2[0][1] = INF
dp2.extend([colorCost[i].copy() for i in range(1, N)])

dp3 = [colorCost[0].copy()]
dp3[0][2] = INF
dp3.extend([colorCost[i].copy() for i in range(1, N)])
# print(dp1)
answer = INF
#Cost 배열을 dp 테이블로 이용하여 최선의 선택을 기록하며 전부 칠한다.
#끝에 값을 고정시킨 테이블을 dp진행시켜서 첫 집의 색을 고정시킨 값을 구하는 dp
#
for i in range(1, N):
    for j in range(3):
        temp = INF
        #현재 j를 칠한다는 기준으로 k색이 j색이랑 동일하지 않은 것중 최댓값을 구한다.
        for k in range(3):
            if j == k:continue
            temp = min(dp1[i-1][k], temp)
        dp1[i][j] += temp
# print(dp1)
answer = min(answer, dp1[-1][0])

for i in range(1, N):
    for j in range(3):
        temp = INF
        #현재 j를 칠한다는 기준으로 k색이 j색이랑 동일하지 않은 것중 최댓값을 구한다.
        for k in range(3):
            if j == k:continue
            temp = min(dp2[i-1][k], temp)
        dp2[i][j] += temp
# print(dp2)
answer = min(answer, dp2[-1][1])
for i in range(1, N):
    for j in range(3):
        temp = INF
        #현재 j를 칠한다는 기준으로 k색이 j색이랑 동일하지 않은 것중 최댓값을 구한다.
        for k in range(3):
            if j == k:continue
            temp = min(dp3[i-1][k], temp)
        dp3[i][j] += temp
# print(dp3)
answer = min(answer, dp3[-1][2])

print(answer)

