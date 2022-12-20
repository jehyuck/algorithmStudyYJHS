import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# 마지막 뽑은수가 Ai일때 가장 긴 부분수열의 길이
D = [0] * N
# 마지막 뽑은수가 Ai일때 가장 긴 부분수열
lis = [[] for _ in range(N)]

# 가장 긴 부분수열의 길이
max_cnt = -1
# 가장 긴 부분수열 중 마지막 수의 인덱스
max_idx = -1

for i in range(N):
    # 초기값
    D[i] = 1
    # 0 ~ i까지 중 가장 긴 부분수열의 마지막 인덱스
    idx = i
    # i-1번째 까지 수 중 A[i]보다 작고 D[i]보다 큰 경우
    for j in range(i):
        if A[j] < A[i] and D[i] < D[j] + 1:
            D[i] = D[j] + 1
            idx = j

    # 최대 길이 보다 큰 경우
    if max_cnt < D[i]:
        max_cnt = D[i]
        max_idx = i

    # 마지막 수가 Ai인 가장 긴 부분수열
    lis[i] = lis[idx][:]
    lis[i].append(A[i])

print(max_cnt)
print(*lis[max_idx])

