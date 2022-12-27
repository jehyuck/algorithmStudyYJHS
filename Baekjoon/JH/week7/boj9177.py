import sys
# from collections import defaultdict
# input = sys.stdin.readline
#
T = int(input()) + 1

for t in range(1, T):
    set1, set2, setTarget = input().split()

    len1 = len(set1)
    len2 = len(set2)

    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    answer = False
    hubo = [[0, len2],[len1, 0]]
    for i in range(len1):
        for j in range(len2):
            if i + j != dp[i][j]: continue
            # print(setTarget[i+j], set1[i],set2[j])
            if setTarget[dp[i][j]] == set1[i]:
                # print("아래", i + 1,j, len1)
                dp[i+1][j] = dp[i][j] + 1
                if i + 1 == len1:
                    hubo[1][1] = j
            if setTarget[dp[i][j]] == set2[j]:
                # print("오른쪽")
                dp[i][j+1] = dp[i][j] + 1
                if j + 1 == len2:
                    hubo[0][0] = i

    # print(dp[hubo[0][0]][hubo[0][1]] == sum(hubo[0]), dp[hubo[1][0]][hubo[1][1]] == sum(hubo[1]))
    if dp[hubo[0][0]][hubo[0][1]] == sum(hubo[0]) and setTarget[dp[hubo[0][0]][hubo[0][1]]:] == set1[hubo[0][0]:]:
        answer = True
    if dp[hubo[1][0]][hubo[1][1]] == sum(hubo[1]) and setTarget[dp[hubo[1][0]][hubo[1][1]]:] == set2[hubo[1][1]:]:
        answer = True
    print("Data set {}: {}".format(t, "yes" if answer else "no"))
    # print(*dp, sep='\n')
