def solution(commands):
    answer = []

    # 보드의 노드
    board = [[p("") for _ in range(51)] for _ in range(51)]

    for i in commands:
        command = i.split()
        cmd = command[0]
        if cmd == 'UPDATE':
            if len(command) == 4:
                r, c = map(lambda x: int(x), command[1:3])
                board[r][c].a = command[3]
            else:
                for j in range(1, 51):
                    for k in range(1, 51):
                        if board[j][k].a == command[1]:
                            board[j][k].a = command[2]
        elif cmd == "MERGE":
            r1, c1 = map(lambda x: int(x), command[1:3])
            r2, c2 = map(lambda x: int(x), command[3:])
            if board[r1][c1] == board[r2][c2] or (r1 == r2 and c1 == c2):
                continue
            if board[r1][c1].a:
                target = board[r2][c2]
                input_data = board[r1][c1]
            elif board[r2][c2].a:
                target = board[r1][c1]
                input_data = board[r2][c2]
            else:
                target = board[r2][c2]
                input_data = board[r1][c1]

            for j in range(1, 51):
                for k in range(1, 51):
                    if target == board[j][k]:
                        board[j][k] = input_data
        elif cmd == "UNMERGE":
            r, c = map(lambda x: int(x), command[1:3])
            temp = board[r][c]
            temp_str = board[r][c].a

            for j in range(1, 51):
                for k in range(1, 51):
                    if temp == board[j][k]:
                        board[j][k] = p("")

            board[r][c].a = temp_str
        else:
            r, c = map(lambda x: int(x), command[1:3])
            answer.append(board[r][c].a if board[r][c].a else 'EMPTY')
    # print(*board)
    return answer

class p:
    def __init__(self, a):
        self.a = a

print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))
print(solution(	["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]))