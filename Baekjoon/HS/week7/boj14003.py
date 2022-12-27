import sys
import bisect
from collections import deque

input = sys.stdin.readline

# 수열 A의 크기
N = int(input())
# 수열 A
A = list(map(int, input().split()))

D, P = [], []
size = 0
LIS = deque()

for num in A:
    # 정렬된 P에 num을 삽입할 위치
    idx = bisect.bisect_left(P, num)
    # A[i]의 삽입 위치를 D[i]에 추가
    D.append(idx)
    # 삽입 위치가 맨끝인 경우
    if size == idx:
        # P에 num 추가
        P.append(num)
        # size 증가
        size += 1
    # 삽입 위치가 끝이 아닌 경우
    else:
        # P[idx]를 num으로 갱신
        P[idx] = num

# LIS 구하기
for i in range(N - 1, -1, -1):
    # size가 0인 경우
    if size < 1:
        break
    # LIS의 뒤에서 부터 찾기
    if D[i] == size - 1:
        # A[i]를 LIS 왼쪽에 추가
        LIS.appendleft(A[i])
        # size 감소
        size -= 1

print(len(LIS))
print(*LIS)
