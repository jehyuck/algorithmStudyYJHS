import sys
from collections import deque


def solution():
    q = deque()
    visited = [[0] * (size2 + 1) for _ in range(size1 + 1)]

    q.append((0, 0, 0))
    visited[0][0] = 1

    while q:
        # 세 단어의 인덱스
        i, j, k = q.popleft()

        # 첫번째 단어의 i번째와 세번째 단어의 k번째가 같은 경우
        if i < size1 and word1[i] == word3[k] and not visited[i + 1][j]:
            q.append((i + 1, j, k + 1))
            visited[i + 1][j] = 1
        # 두번째 단어의 j번째와 세번째 단어의 k번째가 같은 경우
        if j < size2 and word2[j] == word3[k] and not visited[i][j + 1]:
            q.append((i, j + 1, k + 1))
            visited[i][j + 1] = 1

    # 첫번째 단어와 두번째 단어를 섞어서 세번째 단어를 만들 수 있는 경우
    if visited[size1][size2]:
        return True

    return False


input = sys.stdin.readline

T = int(input())
for t in range(1, T + 1):
    # 세 개의 단어
    word1, word2, word3 = map(list, input().split())
    # 세 단어의 길이
    size1, size2, size3 = len(word1), len(word2), len(word3)
    if solution():
        print(f'Data set {t}: yes')
    else:
        print(f'Data set {t}: no')






