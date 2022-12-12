import sys

# input = sys.stdin.readline

# 행 열 이동거리
N, M, K = map(int, input().split())
realK = K + 1
dr = (1, -1, 0, 0)
dc = (0, 0, 1, -1)
# 문자판, 목표문자열, 목표문자열 길이 그 칸에 도달하면 몇개의 답에 도달할 수 있는지 기록할 판.
board = [list(input()) for _ in range(N)]
target = input()
targetN = len(target)
dp = [[[-1]*(targetN + 1) for _ in range(M)] for _ in range(N)]


# dfs와 dp를 통해 답을 구한다.
def dfs(index, r, c):
    global board, target, targetN, dp, N, M, realK

    # 끝에 도달했을 때 1을 반환한다.
    if index == targetN:
        dp[r][c][index] = 1
        return 1

    # 이미 구해놓은 답이 있으면
    if dp[r][c][index] != -1:
        return dp[r][c][index]

    # 없으면 dfs 깊이탐색을 시작한다.
    rtn = 0
    dp[r][c][index] = 0
    for d in range(4):
        nr = r
        nc = c
        for k in range(1, realK):

        # 4방향에 대해서 K길이만큼 탐색을한다.
            nr += dr[d]
            nc += dc[d]
            # 범위 밖으로 나가거나, target과 일치하지 않으면 그만한다.
            if 0 > nr or nr >= N or 0 > nc or nc >= M: continue
            if target[index] != board[nr][nc]: continue

            # rtn += dp[nr][nc][index+1] if dp[nr][nc][index+1] != -1 else dfs(index + 1, nr, nc)
            rtn += dfs(index+1, nr, nc)
    # print(r, c, index)
    dp[r][c][index] = rtn
    return rtn


#시작 문자열과 동일한 문자를 찾으면 dfs를 한다.
answer = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == target[0]:
            idx = 0
            answer += dfs(1, i, j)

print(answer)

'''
dp 초기화의 값으로 사용되는 visit 처리를 0으로 하지말고 -1로 해야함
그 자리에 도착 했을때 끝에 도달하지 않을 수 있다 그 경우를 visit 해줘야하는데 나는 안했었다.

'''