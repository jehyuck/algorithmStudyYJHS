import sys
from collections import deque

input = sys.stdin.readline

# 첫번째 문자열
str1 = list(input().rstrip())
# 두번째 문자열
str2 = list(input().rstrip())

# 두 문자열의 길이
N, M = len(str1), len(str2)
# dp[i][j]: str1[:i]와 str2[:j]의 LCS길이
dp = [[0] * (M + 1) for _ in range(N + 1)]

for i, vi in enumerate(str1, start=1):
    for j, vj in enumerate(str2, start=1):
        # 문자가 같은 경우
        if vi == vj:
            # str1[:i-1]와 str2[:j-1]의 LCS의 길이 + 1
            dp[i][j] = dp[i-1][j-1] + 1
        # 문자가 다른 경우
        else:
            # str1[:i-1]와 str2[:j]의 LCS의 길이, str1[:i]와 str2[:j-1]의 LCS의 길이 중 큰값
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# LCS의 길이
size = dp[N][M]
# LCS
LCS = deque()
# LCS 구하기
R, C = N, M
for i in range(R, 0, -1):
    for j in range(C, 0, -1):
        if dp[i][j] == dp[i - 1][j]:
            break
        elif dp[i][j] == dp[i][j - 1]:
            continue
        else:
            C = j - 1
            LCS.appendleft(str1[i - 1])
            break

print(size)
print(*LCS, sep='')



