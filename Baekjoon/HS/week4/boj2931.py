import sys

# 연결된 파이프 따라 지워진 파이프 찾는 함수
def bfs(start):
    x, y = start
    q = []
    visited = [[0] * (C + 2) for _ in range(R + 2)]

    # 시작 위치 방문 체크
    visited[x][y] = 1

    # 시작 위치와 연결된 파이프 찾기
    for dx, dy in d['+']:
        nx, ny = x + dx, y + dy
        # 파이프가 존재하고 연결된 경우
        if arr[nx][ny] in d and (-dx, -dy) in d[arr[nx][ny]]:
            # 큐에 삽입하고 방문 체크
            q.append((nx, ny))
            visited[nx][ny] = 1
            # 시작 위치 주위에 파이프가 하나만 존재하므로 반복 중단
            break

    while q:
        new_q = []

        for x, y in q:
            for dx, dy in d[arr[x][y]]:
                nx, ny = x + dx, y + dy
                # 방문 여부 확인
                if visited[nx][ny]:
                    continue
                # 연결이 끊긴 경우
                if arr[nx][ny] == '.':
                    # 지워진 파이프 찾기
                    return find_pipe(nx, ny)
                # 새로운 큐에 삽입하고 방문 체크
                new_q.append((nx, ny))
                visited[nx][ny] = 1
        # 큐 갱신
        q = new_q


# 해당 위치에 적합한 파이프 찾기
def find_pipe(x, y):
    # 주위 파이프와 연결될 방향
    con = set()
    for dx, dy in d['+']:
        nx, ny = x + dx, y + dy
        # 주위에 파이프가 존재하고 연결된 경우
        if arr[nx][ny] in d and (-dx, -dy) in d[arr[nx][ny]]:
            # 파이프 방향 추가
            con.add((dx, dy))

    for k, v in d.items():
        # 필요한 파이프 방향들과 일치하는 파이프 찾기
        if con == set(v):
            return (x, y, k)


input = sys.stdin.readline

R, C = map(int, input().split())
arr = [['#'] * (C + 2) for _ in range(R + 2)]

d = {
    '|': [(-1, 0), (1, 0)],
    '-': [(0, -1), (0, 1)],
    '+': [(-1, 0), (0, 1), (1, 0), (0, -1)],
    '1': [(0, 1), (1, 0)],
    '2': [(-1, 0), (0, 1)],
    '3': [(-1, 0), (0, -1)],
    '4': [(0, -1), (1, 0)],
}

for i in range(1, R + 1):
    line = list(input().rstrip())
    for j in range(1, C + 1):
        arr[i][j] = line[j - 1]
        if arr[i][j] == 'M':
            M = (i, j)
        elif arr[i][j] == 'Z':
            Z = (i, j)

answer = bfs(M)
print(*answer)