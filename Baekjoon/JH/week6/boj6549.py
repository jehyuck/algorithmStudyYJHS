import sys
import math as m

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

len_and_arr = list(map(int, input().split()))
answerList = []

# 본 배열, 트리 list, 노드 위치, 시작위치, 끝위치
def init(arr, tree, node, start, end):
    # 요소가 1개일 때에 도달하면 자체를 기록한다.
    if start == end:
        tree[node - 1] = start
    else:
        # 서브트리의 형식으로 양쪽을 나누어 확인한다.
        # 매번 구간 중 가장 낮은 값을 기준으로 그 구간을 기록한다.
        mid = (start + end) // 2 # 중앙값?
        left = node * 2
        right = node * 2 + 1
        # 왼쪽 서브트리와 오른쪽 서브트리를 탐색한다.
        init(arr, tree, left, start, mid)
        init(arr, tree, right, mid + 1, end)

        # 왼쪽과 오른쪽이 실제로 저장된 값을 확인 한다. index - 1에 실제로 저장되게 구현함
        # left - 1, right - 1을 사용하기 편하게 left - 1, left로 사용함
        # print(tree)
        # print(len(arr), len(tree), tree[left], tree[right], node)
        # 더 작은 값의 노드를 현재 노드에 적는다.
        if arr[tree[left - 1]] < arr[tree[left]]:
            tree[node-1] = tree[left - 1]
        else:
            tree[node-1] = tree[left]


def query(arr, tree, node, start, end, x, y):
    # 주어진 범위가 전체 범위를 벗어난 경우
    if x > end or y < start:
        return -1

    # 주어진 범위가 전체 범위 안에 포함되는 경우
    if start >= x and end <= y:
        return tree[node - 1]

    mid = (start + end) // 2
    left = query(arr, tree, node * 2, start, mid, x, y)
    right = query(arr, tree, node * 2 + 1, mid + 1, end, x, y)

    # 한쪽 노드가 범위를 벗어난 경우 자연스럽게 반대쪽 노드가 선택됨
    if left == -1:
        return right
    elif right == -1:
        return left
    else:
        # 둘중에 더 작은 값을 선택
        if arr[left] >= arr[right]:
            return right
        else:
            return left

# 답을 분할정복을 통해 구하는 함수.
def dac(start, end):

    # 현재 구간에서 최솟값 인덱스를 구한다.
    index = query(arr, tree, 1, 0, N - 1, start, end)

    #단일 블럭인 경우 현재 위치를 반환
    if abs(end - start) == 0:
        return arr[index]

    # 답일 경우 3가지를 미리 선언 해 준다.
    # v1 = 가장 낮은 블럭의 높이 * 히스토그램의 길이
    v1, v2, v3 = arr[index] * (end - start + 1), 0, 0

    # 범위가 벗어나지 않을 경우 분할한다.
    if index-1 >= start:
        v2 = dac(start, index-1)
    if index+1 <= end:
        v3 = dac(index+1, end)
    return max(v1, v2, v3)

# 풀이의 본문이다. 길이가 0 인 테스트 케이스가 나올 때까지 문제를 풀이한다.
while len_and_arr[0] != 0:

    # 길이는 입력받은 arr의 첫 문자
    N = len_and_arr[0] # 길이
    arr = len_and_arr[1:] # 배열
    tree = [0] * (2 ** (m.ceil(m.log2(N) + 1)) - 1) # 세그먼트 트리 초기화

    init(arr, tree, 1, 0, N-1) # arr을 세그먼트 트리(tree)에 담는 함수
    # print(tree)
    answerList.append(dac(0, N-1))
    # print(tree)
    len_and_arr = list(map(int, input().split()))
print(*answerList, sep='\n')