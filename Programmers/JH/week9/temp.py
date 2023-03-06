import math
N = input()

n = len(N)
dp = [[0] * 10 for _ in range(n)]

for i in range(10):
    dp[0][i] = 1

for i in range(1, n-1):
    temp = sum(dp[i-1])
    for j in range(0, 10):
        if j != 1:
            dp[i][j] = temp
        else:
            dp[i][j] = temp - dp[i-1][3]
sums = sum(dp[-2])
for i in range(0, int(N[0])):
    if i != 1:
        dp[-1][i] = sums
    else:
        dp[-1][i] = sums - dp[-2][3]

answer = 0  if N[-2:] == '13' else 1
sub = [sum(dp[n-1-i][:int(N[i])]) for i in range(1, n)]
for i in range(0, n-1):
    crt = int(N[i])
    for j in range(crt):
        print(j)
        if j == 3 and N[i+1] == '1':
            continue
        answer += dp[i][j]
answer += sum([sum(dp[i][1:]) for i in range(n)])
print(*dp)
print(answer)