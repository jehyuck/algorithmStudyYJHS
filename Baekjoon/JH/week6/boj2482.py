# 두 수 입력
N = int(input())  # 색상환 갯수
K = int(input())  # 선택할 색의 갯수
n = N - 1
# N개의 색 중 K개를 고름
# N개의 색 모든 경우에 K번째 골릴 경우의 수까지 생각해서 N * K크기의 테이블을 생성
dp = [[[0, 0] for _ in range(N)] for _ in range(K)]
dp[0] = [[1, 1] for _ in range(N)]
dp[0][0][0] = 0

# dp 1
startC = 0
startF = 2

# dp[k][i][0] = i번째 색을 k번째 색으로 선택했을 때 나올 수 있는 경우의 수(첫번째 색을 제외하고)
# dp[k][i][0] = i번째 색을 k번째 색으로 선택했을 때 나올 수 있는 경우의 수(첫번째 색을 포합하고)
# k를 1씩 올린다.
for i in range(1, K):
    # k번째 색으로 j를 고를 때
    # 반복 횟수를 줄이기 위해 startF를 2씩 올리며 탐색한다.
    for j in range(startF, N):
        jj = j - 1
        # k번째 색으로 j번색을 선택하는 수를 구하기 위해 위에 등장한 경우의 수를 전부 더한다.
        for q in range(startC, jj):
            # 끝의 값을 알맞게 구하기 위해 첫번째 색을 제외한 경우를 따로 구함
            dp[i][j][0] += dp[i - 1][q][0] % 1000000003
            # 끝의 값을 제외한 수를 알맞게 구하기 위해 전부 구한다.
            dp[i][j][1] += dp[i - 1][q][1] % 1000000003

    # 반복 횟수를 줄이기 위해 시작지점을 변수로 따로 관리
    # 행마다 시작지점이 2씩 커지기 때문에
    # 현재 시작지점 +2 이전 시작지점 +2 해준다.
    startC += 2
    startF += 2

# 답을 구하기 위해 K번째 수들의 총 합을 구한다.
# 끝의 경우에만 따로 k,n,0을 통해서 구해준다.
answer = 0
for i in range(n):
    answer += dp[-1][i][1] % 1000000003
answer = (answer + dp[-1][-1][0]) % 1000000003
# print(*dp, sep='\n')
print(answer)