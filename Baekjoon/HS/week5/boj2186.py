import sys
from collections import defaultdict

input = sys.stdin.readline

# 상 하 좌 우
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# board: NxM 크기의 문자판, K: 상하좌우 이동할 수 있는 칸, word: 영단어
N, M, K = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
word = input().rstrip()

# 영단어 길이
word_size = len(word)

# i행 j열의 문자를 끝으로 영단어의 idx번째까지 만들 수 있는 경로 개수
dp = [[[0] * word_size for _ in range(M)] for _ in range(N)]

# 문자판에 있는 문자들의 좌표
pos = defaultdict(list)

for i in range(N):
    for j in range(M):
        # 문자판의 문자들의 좌표 추가
        pos[board[i][j]].append((i, j))
        # 영단어의 첫문자일 경우
        if board[i][j] == word[0]:
            dp[i][j][0] = 1

for idx in range(word_size - 1):
    # 영단어의 idx번째 문자
    alpha = word[idx]
    # 영단어의 idx+1번째 문자
    next_alpha = word[idx + 1]
    # idx번째 문자의 위치
    for x, y in pos[alpha]:
        # 가능한 경로가 없는 경우
        if dp[x][y][idx] == 0:
            continue
        for dx, dy in d:
            for k in range(1, K + 1):
                # 현재 위치에서 상하좌우로 k만큼 떨어진 위치
                nx, ny = x + k * dx, y + k * dy
                # 문자판 범위 밖인 경우
                if not (0 <= nx < N and 0 <= ny < M):
                    break
                # 다음 위치의 문자가 idx+1번째 문자가 아닌 경우
                if board[nx][ny] != next_alpha:
                    continue
                # 다음 위치에 idx+1번째 문자가 올 경로 수 갱신
                dp[nx][ny][idx + 1] += dp[x][y][idx]

# 영단어를 만들 수 있는 경로의 개수
answer = 0
for i in range(N):
    for j in range(M):
        answer += dp[i][j][-1]
print(answer)







