import sys

input = sys.stdin.readline

INF = int(1e9)

# 집의 수
N = int(input())
# 집을 빨강, 초록, 파랑으로 칠하는 비용
cost = [list(map(int, input().split())) for _ in range(N)]

# 첫번째 집 색을 기준으로 i번째까지 칠하는 방법 중 i번째 집을 해당 색으로 칠하는 최소 비용
dp = [[[INF] * 3 for _ in range(N)] for _ in range(3)]

# 모든 집을 칠하는 비용의 최솟값
answer = INF

# 첫번째 집의 색
for fc in range(3):
    dp[fc][0][fc] = cost[0][fc]
    # 집의 수 만큼 반복
    for i in range(1, N):
        # i번째 집을 칠할 색
        for c in range(3):
            # i-1번째 집 색
            for bc in range(3):
                # i번째 집과 i-1번째 집의 색이 같은 경우
                if c == bc:
                    continue
                # i번째 집을 해당 색으로 첫번째 집부터 i번째 집까지 칠하는 최소 비용 갱신
                dp[fc][i][c] = min(dp[fc][i][c], dp[fc][i-1][bc] + cost[i][c])
    # 마지막 집의 색
    for lc in range(3):
        # 첫번째 집과 마지막 집의 색이 같은 경우
        if fc == lc:
            continue
        # 최소 비용 갱신
        answer = min(answer, dp[fc][N-1][lc])

print(answer)
