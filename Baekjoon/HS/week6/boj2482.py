import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# 색상환에 포한된 색의 개수
N = int(input())
# 선택할 색의 개수
K = int(input())
# 나눌 수
MOD = 1_000_000_003

# DP[i][j]: j색상환에서 어떤 인접한 두 색도 동시에 선택하지 않고 i개의 색을 선택하는 경우의 수
# D: 첫번째 색을 포함한 경우
D = [[0] * (N + 1) for _ in range(K + 1)]
# P: 첫번째 색을 포함하지 않는 경우
P = [[0] * (N + 1) for _ in range(K + 1)]

# 1개의 색을 선택하는 경우
for j in range(1, N + 1):
    D[1][j] = 1
    P[1][j] = j - 1

# 2개 ~ K개의 색을 선택
for i in range(2, K + 1):
    for j in range(2, N + 1):
        D[i][j] = (D[i - 1][j - 2] + D[i][j - 1]) % MOD
        P[i][j] = (P[i - 1][j - 2] + P[i][j - 1]) % MOD


answer = (D[K][N - 1] + P[K][N]) % MOD
print(answer)

