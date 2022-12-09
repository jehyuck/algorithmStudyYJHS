INF = int(1e9)


def solution(alp, cop, problems):
    # 모든 문제를 풀기 위한 목표 알고력과 코딩력
    alp_target, cop_target = 0, 0
    for alp_req, cop_req, _, _, _ in problems:
        alp_target, cop_target = max(alp_target, alp_req), max(cop_target, cop_req)

    # (알고력 a, 코딩력 c) 상태에 도달하는 데 필요한 최단 시간
    dp = [[INF] * (cop_target + 1) for _ in range(alp_target + 1)]

    # 초기 알고력과 코딩력은 목표 알고력과 코딩력을 넘으면 안된다.
    alp, cop = min(alp, alp_target), min(cop, cop_target)
    dp[alp][cop] = 0

    for a in range(alp, alp_target + 1):
        for c in range(cop, cop_target + 1):
            # (현재 알고력 + 1)이 목표 알고력 보다 작은 경우
            if a + 1 <= alp_target:
                # (현재 알고력 + 1, 현재 코딩력) 갱신
                dp[a + 1][c] = min(dp[a + 1][c], dp[a][c] + 1)
            # (현재 코딩력 + 1)이 목표 코딩력 보다 작은 경우
            if c + 1 <= cop_target:
                # (현재 알고력, 현재 코딩력 + 1) 갱신
                dp[a][c + 1] = min(dp[a][c + 1], dp[a][c] + 1)
            # 모든 문제에 대해서...
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                # 문제를 푸는데 필요한 알고력, 코딩력을 만족하지 못하는 경우
                if not (alp_req <= a and cop_req <= c):
                    continue
                # 문제를 푼 후 알고력과 코딩력은 목표 알고력과 코딩력을 넘으면 안된다.
                na, nc = min(a + alp_rwd, alp_target), min(c + cop_rwd, cop_target)
                # 문제를 푼 후 알고력과 코딩력을 얻는 최단시간 갱신
                dp[na][nc] = min(dp[na][nc], dp[a][c] + cost)

    # 모든 문제를 풀 수 있는 알고력과 코딩력을 얻는 최단시간
    answer = dp[alp_target][cop_target]
    return answer


# 입출력 예
alp = 10
cop = 10
problems = [[10,15,2,1,2],[20,20,3,3,4]]
result = 15

print(result == solution(alp, cop, problems))