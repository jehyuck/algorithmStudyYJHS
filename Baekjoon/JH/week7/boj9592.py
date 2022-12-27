import sys
from collections import deque as d
# input = sys.stdin.readline

#두 문자열을 입력 받음
str1, str2 = list(input()), list(input())
len1, len2 = len(str1), len(str2)

# dp를 사용한다. dp[i][j] = 이때까지 탐색한 것중 가장 긴 길이, 이전 것의 idx
# i = str1의 위치, j = str2의 위치
dp = [[[0, (0, 0)] for _ in range(len2 + 1)]  for i in range(len1 + 1)]

for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        if str1[i-1] == str2[j-1]:
            dp[i][j][0] = dp[i-1][j-1][0] + 1
            dp[i][j][1] = (i-1, j-1)
        else:
            if dp[i-1][j][0] > dp[i][j-1][0]:
                dp[i][j][0] = dp[i-1][j][0]
                dp[i][j][1] = dp[i-1][j][1]
            else:
                dp[i][j][0] = dp[i][j-1][0]
                dp[i][j][1] = dp[i][j-1][1]
trace = dp[-1][-1]
count = trace[0]
answer = d()
print(count)
# print(*dp, sep='\n')

while count > 0:
    if trace == (0, 0):
        break
    count -= 1
    i, j = trace[1]
    answer.appendleft(str1[i])
    trace = dp[i][j]
print(''.join(answer))
