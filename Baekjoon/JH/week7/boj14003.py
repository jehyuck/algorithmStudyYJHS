import sys
import bisect as b
from collections import deque as d

# input = sys.stdin.readline

N = int(input())

li = tuple(map(int, input().split()))
track = [None] * N
count = 1
dp = [li[0]]
idxDp = [0]
track[0] = -1
answer = 0

for i in range(1, N):
    ele = li[i]
    idx = b.bisect(dp, ele)
    # print(dp)
    # print(ele, idx)
    if idx >= len(dp):
        if dp[-1] == ele:
            continue
        dp.append(ele)
        idxDp.append(i)
        track[i] = idxDp[idx - 1] if idx != 0 else -1
        answer = i
    else:
        # print(dp[idx], ele)
        if dp[idx-1] == ele:
            continue
        dp[idx] = ele
        idxDp[idx] = i
        track[i] = idxDp[idx - 1] if idx != 0 else -1

que = d()
t = track[answer]
que.append(li[answer])

while t != -1:
    # print(t, end=' ')
    que.appendleft(li[t])
    t = track[t]

# print(*track)
# print()
# print(*li)
print(len(que))
print(*que)
# print(len(dp))
# print(*dp)
# print(*idxDp)


