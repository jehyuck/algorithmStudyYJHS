import sys

input = sys.stdin.readline

while True:
    line = list(map(int, input().split()))
    # 직사각형의 수
    n = line[0]
    # 반복 중단 조건
    if n == 0:
        break
    # 히스토그램에 있는 직사각형의 높이
    h = line[1:]

    # 스택
    stack = []
    # 히스토그램에서 가장 넓이가 큰 직사각형의 넓이
    answer = 0

    for i in range(n):
        # 스택의 top에 있는 값이 현재 직사각형의 길이 보다 큰 경우
        while stack and h[stack[-1]] > h[i]:
            # 스택에서 pop
            tmp = stack.pop()

            # 직사각형의 너비 구하기
            if not stack:
                width = i
            else:
                width = i - stack[-1] - 1

            # 직사각형의 넓이 갱신
            answer = max(answer, width * h[tmp])
        # 스택에 현재 직사각형 추가
        stack.append(i)

    while stack:
        # 스택에서 pop
        tmp = stack.pop()

        # 직사각형의 너비 구하기
        if not stack:
            width = n
        else:
            width = n - stack[-1] - 1

        # 직사각형의 넓이 갱신
        answer = max(answer, width * h[tmp])

    print(answer)




