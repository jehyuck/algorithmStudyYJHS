from collections import deque as d

N = int(input())
arr = tuple(map(int, input().split()))

# 첫번째에는 길이, 두번째에는 바로앞의 index를 기록하는 dp 테이블을 생성한다.
dp = [[1, -1] for _ in range(N)]

# 0 ~ i전까지 가장 큰 길이를 갖는 index = k
# dp[i] = [dp[k][0]+1, k] (n까지 실행)
# 답이 dp[-1]에 저장됨
# 역추적 하여 답을 출력한다.
answer = [1, -1]
answerI = 0
for i in range(1, N):
    for j in range(0, i):
        if arr[i] > arr[j] and dp[j][0] >= dp[i][0]:
            dp[i][0] = dp[j][0] + 1
            dp[i][1] = j

    if answer[0] < dp[i][0]:
        answer = dp[i]
        answerI = i

answerD = d([arr[answerI]])

while answer[1] != -1:
    answerD.appendleft(arr[answer[1]])
    answer = dp[answer[1]]

print(len(answerD))
print(*answerD)
