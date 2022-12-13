import sys


# TSP
def travel():
    # v0을 제외한 부분집합의 개수
    size = 2 ** (N - 1)
    # D[i][A] : A에 속한 도시를 각각 한 번씩만 거쳐서 vi에서 v0으로 가는 최소 비용
    D = [[float('inf')] * size for _ in range(N)]

    # V의 부분집합 A가 공집합인 경우
    for i in range(1, N):
        # vi에서 v0으로 바로 가는 비용
        D[i][0] = W[i][0]

    # k: 부분집합의 개수
    for k in range(1, N - 1):
        # A: 부분집합
        for A in range(1, size):
            # k와 A의 부분집합의 개수가 일치하지 않는 경우
            if count(A) != k:
                continue
            # i: 원소(도시)
            for i in range(1, N):
                # 부분집합 A에 원소 i가 포함된 경우
                if is_in(i, A):
                    continue
                # i에서 시작해서 A에 속한 도시를 거쳐서 v0으로 가는 최소 비용 갱신
                D[i][A] = minimum(D, i, A)

    # 부분집합에 v0을 제외한 모든 도시가 속한 경우
    A = size - 1
    # v0에서 모든 도시를 거쳐서 v0으로 가는 최소 비용 갱신
    D[0][A] = minimum(D, 0, A)
    return D[0][A]


# 부분집합 A의 원소의 개수를 구하는 함수
def count(A):
    cnt = 0
    for i in range(1, N):
        # i가 A에 속한 경우
        if A & (1 << (i - 1)) != 0:
            # 개수 증가
            cnt += 1
    return cnt


# A에 vi 원소가 포함되는지 획인하는 함수
def is_in(i, A):
    if (A & (1 << (i - 1))) != 0:
        return True
    else:
        return False


# i에서 시작해서 A에 속한 도시를 거쳐서 v0으로 가는 최소 비용 구하는 함수
def minimum(D, i, A):
    # 최소 비용
    min_value = float('inf')
    # j: i 다음으로 지나갈 도시
    for j in range(1, N):
        # j가 부분집합 A에 속한 경우
        if is_in(j, A):
            # i -> j -> 나머지 부분집합의 도시를 거쳐서 v0으로 가는 비용
            m = W[i][j] + D[j][diff(A, j)]
            # i에서 A에 속한 도시를 거쳐서 v0으로 가는 최소 비용 갱신
            min_value = min(min_value, m)
    # 최소 비용 반환
    return min_value


# A - {vj}: 차집합 구하는 함수
def diff(A, j):
    t = 1 << (j - 1)
    return A & (~t)


input = sys.stdin.readline

# 모든 도시의 수
N = int(input())
# 주어진 그래프의 인접 행렬
W = [list(map(int, input().split())) for _ in range(N)]

# 도시 i에서 j로 갈 수 없는 경우 -> INF
for i in range(N):
    for j in range(N):
        if not W[i][j]:
            W[i][j] = float('inf')

# 외판원의 순회에 필요한 최소 비용
answer = travel()
print(answer)