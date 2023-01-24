from collections import deque as d

def solution(n, m, x, y, r, c, k):
    answer = ''
    # 사전순으로 방향을 정렬
    str_order = "dlru"

    # 방향 정의
    dr = (1, 0, 0, -1)
    dc = (0, -1, 1, 0)

    # k길이 경우의 수에 대해 visit을 만들어줌
    visit = [[[False] * m for _ in range(n)] for _ in range(k+1)]

    # deque를 이용
    que = d()

    # 처음 위치로 시작
    que.append((x - 1, y - 1, ""))

    count = 0
    # bfs
    # count가 끝까지 가거나도달하지 못했으면 종료
    while que and count < k:
        # count를 계속 올려준다.
        temp_que = d()
        for q in que:
            crt_r, crt_c, crt_str = q

            for i in range(4):
                nr = crt_r + dr[i]
                nc = crt_c + dc[i]

                # 다음 위치가 이미 간 위치면
                # print(nr, nc)
                if 0 > nr or nr >= n or 0 > nc or nc >= m: continue
                if visit[count][nr][nc]:
                    continue

                visit[count][nr][nc] = True
                temp_que.append((nr, nc, crt_str + str_order[i]))
        count += 1
        que = temp_que
        # print(que)
    r -= 1
    c -= 1
    for i in que:
        if r == i[0] and c == i[1]:
            answer = i[2]
            break
    return answer

print(solution(	3, 4, 2, 3, 3, 1, 5))