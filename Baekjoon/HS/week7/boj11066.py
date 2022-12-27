import sys

input = sys.stdin.readline

# 테스트 케이스 수
T = int(input())

for _ in range(T):
    # 파일 개수
    K = int(input())
    # 파일 크기
    files = list(map(int, input().split()))
    # 구간합 0 ~ i번째 파일까지
    total = [0] * (K + 1)
    total[0] = files[0]
    for i in range(1, K + 1):
        total[i] = total[i-1] + files[i - 1]

    # dp[i][j]: i부터 j까지 파일을 합치는데 드는 최소비용
    dp = [[0] * (K + 1) for _ in range(K + 1)]

    # 대각선 기준으로 떨어진 거리
    for k in range(1, K):
        for i in range(1, K - k + 1):
            j = i + k

            # i부터 j까지 파일 합
            dp[i][j] = total[j] - total[i - 1]
            # 최소 비용
            _min = int(1e9)
            # 최소 비용 구하기
            for d in range(j - i):
                _min = min(_min, dp[i][i + d] + dp[i + d + 1][j])
            # 최소 비용 더하기
            dp[i][j] += _min

    # 1부터 K까지 파일을 합치는데 드는 최소비용
    print(dp[1][K])




