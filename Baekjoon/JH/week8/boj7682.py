
# 입력

# 방문 set
sets = set()
# 정답 set
answer_set = set()
sets.add(".........")

upper = set([(1, 1), (0, 2), (2, 0)])
lower = set([(0, 0), (1, 1), (2, 2)])


def check(r, c, arr, target):
    idx_tuple = (r, c)
    # print(idx_tuple)
    count = 0
    for k in range(3):
        if target == arr[k][c]:
            count += 1
    if count == 3:
        return False

    count = 0
    for k in range(3):
        if target == arr[r][k]:
            count += 1
    if count == 3:
        return False

    count = 0
    if idx_tuple in upper:
        for rr, cc in upper:
            if arr[rr][cc] == target:
                count += 1
    if count == 3:
        return False

    count = 0
    if idx_tuple in lower:
        for rr, cc in lower:
            if arr[rr][cc] == target:
                count += 1
    if count == 3:
        return False
    return True





# 모든 경우의 수 찾기
def find_all(start, turn, turn_count):
    # 턴에 맞는 target 지정
    crt = 'X' if turn else 'O'

    # 모든 칸에 대해서 방문하지 않았으면 체크를 한다.
    for i in range(3):
        for j in range(3):
            if start[i][j] != '.':
                continue

            # list는 객체이기 때문에 새로운 board판을 넘기기 위해 새로운 객체 생성
            nextt = [a.copy() for a in start]
            nextt[i][j] = crt

            # set 체크를 위해 객체를 문자열 값으로 바꿔준다.
            check_set = ''.join([''.join(a) for a in nextt])

            # 마지막 칸에 놓기가 성공하면 답에 저장
            if turn_count == 8:
                answer_set.add(check_set)
                continue

            # 똑같은 값이 있다면 하지 않는다.
            if check_set not in sets:
                sets.add(check_set)
                # print(check_set, end ='')

                # 정답이면 answer에 기입, 아니면 dfs 진행
                if check(i, j, nextt, crt):
                    find_all(nextt, not turn, turn_count + 1)
                else:
                    answer_set.add(check_set)


find_all([['.','.','.'],['.','.','.'], ['.','.','.']], True, 0)
print(answer_set)
inputs = input()
while len(inputs) != 3:
    print('valid' if inputs in answer_set else 'invalid')
    inputs = input()



############# ver 2

answer_set = {'XOX.XOX.O', 'OOOXX...X', 'XOOXO.X.X', 'X.OXOXOOX', 'X.OOXX.OX', 'XXXOX..OO', 'OXXOOO.XX', 'OXOXOX.XO', '.XOO.OXXX', '.XOXOXOXO', '.X.OOO.XX', 'OOXXO.XXO', 'OOXXOXOXX', 'XOO.XOXXO', 'X.OXXOXO.', 'O.X.O.XXO', 'X.OOXOXXO', 'OOX.XXX.O', '.XOOOXOXX', 'XXXXO..OO', '.XO..OXXO', 'O.XO.XXOX', '.OX..X.OX', 'X.OX.OX..', 'XXOXX.OOO', 'XXXO..OOX', 'XXOOOXOX.', 'O.X.XOXOX', '.OXOXX.OX', 'O.O.OXXXX', '..XOXOXOX', '.O.XOX.OX', 'XXOOXXXOO', 'XXOX.O..O', 'XOX.X.XOO', 'XOOXOX.OX', 'OXXOX.OOX', 'OX.OXO.XX', '..XOX.X.O', 'OX.XOX..O', 'XOXXXOOXO', 'XXXOOXO..', '.XOXXOOX.', 'O.X.X.X.O', '.XXXXOOOO', 'OOO..XXX.', 'XXOXOOXOX', 'XXOXO.O..', 'X.OX.XXOO', 'X.O.XO..X', 'XXXOOXXOO', 'OOXOX.X.X', 'OX.OX..X.', 'OOXOXOXXX', 'OXXOXXXOO', '..XOXOXXO', 'OXXOOOX.X', '.X.OX..XO', 'XOO.X.XOX', 'OO.XXXO.X', 'X.OOO.XXX', 'OXX.XOXO.', 'OOX..XOXX', 'OX.OXOXX.', 'O.XO..OXX', 'XOX.X.OOX', 'XXXXOOOXO', '..XOOO.XX', 'X.XOXO.OX', 'XXXOO.XO.', 'OXO.OXXXO', 'XXOOXXOOX', 'XXXOO..OX', 'X.OOX...X', '.XX.XOOXO', 'XOO.X...X', 'X.OXO.X..', '..O.O.XXX', 'O.XXOX..O', 'X.O.XOXOX', '.XOOXX.XO', 'XOXO.X.OX', 'X.OX..XO.', 'XOXOXOXXO', 'OXO.X..X.', '.XOOXXOX.', '..OXXX.O.', 'XOOXX..OX', 'XOOX.OXX.', 'XOO.XX.OX', '.XOXO.OX.', '.O.XOOXXX', 'O..OXXO.X', 'XX.OXXOOO', '..X.XOXO.', 'XOOOXX..X', 'XO.XXXO.O', '.X..X.OXO', 'OXOOXOXXX', 'X..XX.OOO', 'XXX.OO.XO', 'XOOXOXOX.', 'X.OOX.OXX', 'O.XXOOXXO', 'OOXXXX..O', '.XOOO.XXX', 'XOXOX.XO.', 'XXO.OXOOX', 'XXX.OXOO.', 'X.XOX.OOX', 'OX..XOOXX', '.OXOOX.XX', 'XOXXOXOXO', 'XX.OOOXXO', '..XXXOXOO', 'XX.OXOOX.', 'X..OXXOOX', '.XXO.XOOX', 'XO.XO.X..', 'X.OXOXO..', 'OXXOXXO.O', 'X.XOXOX.O', 'OXO.X.XXO', '.XO.X..XO', '.XOOX..X.', 'X.XO.XOOX', 'OOOXX.XOX', 'O.XXO.X.O', 'XXOX.XOOO', 'X.OXXXOO.', 'XXXO.OOX.', 'OXXOOXXOX', 'XXOOXO.X.', 'O.XOXXOXO', 'XXXX.OOO.', 'O.XOOX.XX', '..X.OXO.X', 'XOOXXO.XO', 'XX.OOO..X', 'OXXXO.OXO', 'XOXOOX..X', 'O.OXXXX.O', 'OXOXO.XXO', 'OOOX.XXXO', '.OOXXXXO.', '.OOXXX.XO', 'XOXOXO..X', '..OO..XXX', 'OOXOXXX..', '..X..XOOX', '.X.XXOOXO', 'XO.OX.XOX', '..OXXX..O', '..XOXXXOO', 'O.OXOXOXX', '.O..O.XXX', '.OX.O.XOX', 'O.X.OX..X', 'XOX.O.XO.', '.OX.XXXOO', 'X..X.OX.O', 'XX.OXO.OX', '.XX..XOOO', 'OOOX..X.X', 'X.OXOXX.O', 'XOX.OOXOX', 'XXOXO.XO.', 'OXXO..OX.', 'XXX.XO.OO', '.OOOX.XXX', 'XO.XXOXO.', 'XXXOXOO..', 'XXOOXXOXO', '.OXXO.XO.', 'X..XOOXXO', 'XXXO...O.', 'OXX.O..XO', 'O.XXOXOXO', '.OXOXXO.X', 'OO.XXXOX.', 'XO..XXOOX', 'XOOX..XXO', 'XOOXX.O.X', 'XXOOO.OXX', 'XXX.O.OOX', 'O.OXXX...', '.OOXXOXXO', 'XXXOXO.O.', 'O.XOXOX.X', 'X.OXOXXO.', 'XXX.OO...', 'XXX....OO', '...XXXO.O', '..O..OXXX', 'XXX.XOO.O', 'XXXO.O.OX', 'O..XXX..O', 'XOXXO.OOX', 'OOOXXO.XX', 'XXO.X.OXO', '.O..OXXOX', 'XOO.X.OXX', 'XOX.XOXO.', 'OXO.XO.XX', 'O.XOX.XOX', 'OXOXXOXOX', 'O.XXO..XO', 'OX.OOXXXO', 'XXO.OOXXO', 'O.X.OOXXX', 'XXO.OXO..', '.XO.XXOXO', 'XX.XOXOOO', 'OXX.OX..O', 'OX.XXXOO.', 'OOXXX.XO.', 'XOOX.XX.O', 'X.OOXOX.X', 'OXOXX..XO', '.X.XX.OOO', 'OOX.OX.XX', 'XXXO..OXO', 'XXX.OOOX.', 'OXXOXXOO.', 'O.XXXXOO.', 'XXXOOX..O', 'OO.XO.XXX', 'OXOXOXO.X', 'O.XXOXO.X', 'X.XXOOX.O', 'OOXOXXXOX', '...O.OXXX', 'OXO.OXOXX', '.OX.OXOXX', 'X.XOXOO.X', 'O.XOXXXO.', 'OOXXXX.O.', 'OX.XXX.OO', 'XOOXOXXXO', 'OXXOOX.XO', 'O.XOXXO..', 'OX.XOXOXO', '...XXXOO.', 'X.XOXXOOO', '.OXOX.XXO', 'XOXOXXOXO', '.OX.XOXXO', 'OXXXOXO.O', 'XXO.XO..O', 'XXXXOOXOO', 'OXX.OXO.X', 'XOOO..XXX', 'X.XXOOXO.', 'O..XXXOXO', 'OOXXO.XOX', 'XO.OXXO.X', 'OOXXXXXOO', 'OOXOX.XX.', 'OX.OXX.XO', '.XXOOX.OX', '..XOOXOXX', 'X..X.XOOO', 'XOX.OXO.X', 'XOXXOXOO.', 'OOXXXXO..', 'OO..XOXXX', 'X.OOXXO.X', 'XXXOOXOXO', 'OXXXOOXOX', 'X.XXO.XOO', 'X..OOO.XX', 'OOX.XXXO.', '.OOXO.XXX', 'XXOX..XOO', 'X.OOOXOXX', '.X.OOOX.X', 'OOXXXXOXO', 'XXX..OO..', 'OOOXX.X..', 'OOOXOX.XX', 'XXXOO.O.X', 'X.O.XOOXX', 'OXOXO.OXX', 'O..XO.XXO', 'O.XXXOXO.', 'O.XOXX.OX', 'XOOXOXX..', '.XOOXO.XX', 'X..XXOXOO', 'XOXOXOXOX', 'XOX.OXXOO', 'OXO.XX.XO', 'XXO..O.XO', 'OOXX.XO.X', '..OX.OXXO', 'O.OXXXOX.', 'OX..X..XO', 'XO.XX.OOX', 'OXX.XO.XO', 'OXX.OXXOO', 'XXXXOO.O.', '.O.XOXXO.', 'XXXO.X.OO', 'XOO.OXXOX', 'XXX..OOOX', 'X..XO.X.O', 'OX.O..OXX', '.XOXXXO.O', 'X.OXX.XOO', 'X.O..OXXO', '.XXOXOXO.', 'X.XOX.XOO', 'X...XXOOO', 'OO.XXX.OX', 'X.OXOOX.X', 'XX.OOOX..', 'OOO.X..XX', '.OXXXOX.O', 'XXX.O...O', '.XOX.OX.O', 'XOOX..XOX', '.XOXXX.OO', 'OX..OOXXX', 'OXOXXXXOO', '..X.OX.OX', 'XXO.X.OOX', 'OOXOXXOX.', 'XOXOX.X.O', 'OXXOXOXXO', 'XO.OX.OXX', 'XXOOOXO.X', 'O.OXXX.OX', '.OXXOX.O.', 'X.XOOX.OX', '.OXXO..OX', 'XXXXO.O.O', 'XOXXOO.OX', 'XX..XOOOX', '.X.OOOXX.', 'OXXOO.OXX', 'OOOXXOX.X', 'X...XOO.X', '.OXXX.XOO', '.XXOXOX.O', 'O.XOXOXX.', '.XOXXOXOO', 'XXOOX..OX', 'XOOXXOOXX', 'OXOOXXXXO', '.XXOXXOOO', 'O..XXXOOX', 'XOXOO.XOX', 'XXOOXO..X', 'OX.OX.O.X', 'XO.O.OXXX', '.OXOO.XXX', 'OOXXOXX.O', 'XOOX.OX.X', 'X.XOOO..X', 'XOOXXXOOX', '..OXOXOX.', 'OXOO..XXX', 'OOXXOXXO.', 'XO.XX.XOO', '.XO.O.OXX', 'OOX.OXXXO', '.OX.OXXO.', 'O.O.XOXXX', '.X.OXXOXO', '.X.OXOOXX', 'OOOX.X.X.', 'XOXX.OX.O', '.X..XO.XO', 'XXOOX.O.X', '.XXOXOOX.', 'X..OXOXOX', '.OOXXXX.O', 'XX.OXOO.X', 'XO.XOOXX.', '.OOXOXXOX', '.XXOX.XOO', '.O.XXXOOX', 'O....OXXX', 'OXXXXOOXO', 'OOXOOXXXX', 'OOOXOXX.X', 'XOXOOO.XX', 'OX.XXO.XO', '.XOXX.OXO', 'OXOOXX.X.', 'XXXO....O', 'XO.XOXOOX', '.OXOOXX.X', 'XXOXOOO.X', '.XOXOOOXX', 'OXX.OOXXO', '.O...OXXX', '.OXOXOX.X', 'X.OXO.XXO', '.OX..XO.X', 'XOXOOOX.X', 'OXOOXXO.X', 'X.OXO.XOX', 'XXX.O..O.', 'XXX...O.O', '.OX.X.X.O', 'X.O.OXO.X', 'OXXOX.X.O', 'X.XOOOXOX', '.OXO.OXXX', 'OX.O.OXXX', 'O..XOOXXX', 'OOXXX.X.O', 'O.XOX.O.X', '.OXXXXOO.', '.X..XOOX.', 'XXX...OO.', '.XOXXXOO.', 'OOX..XXOX', 'XXOXOXO.O', 'XOOOX..XX', '..X.XXOOO', 'XX.OOOXOX', 'XXXOO.X.O', 'XO.XXOX.O', 'OXXO.OOXX', 'XOX.XO.OX', 'OXO..OXXX', 'O.OOX.XXX', 'OXXXOOOXX', 'O.OXXXO.X', 'XOOOXOXXX', 'X.O.O.OXX', 'XXOO.OXXO', 'XXXOXOOXO', 'XOXX.XOOO', 'OO.XOXXXO', '..XOOXXOX', 'O.OXXX.XO', '.OXXXXO.O', 'XOOXXX.O.', '..OXXO.XO', 'OXO.XXOX.', 'O..XXXO..', 'X.OX..X.O', 'XXOXOXOO.', 'OXOXXXOOX', 'XO.OXOX.X', 'X.OXOOOXX', 'XOXOOOXX.', 'X.X.X.OOO', 'O.OXXOXXO', 'O..OXOXXX', 'OXOXOOXXX', 'X.O.OXOX.', 'OXXOX..XO', '..OOOXXXX', 'X.X.OXOOX', 'OX.O.XO.X', 'O.XOX.X..', '..O.XOXXO', 'XXO.XOOX.', 'OOX..OXXX', 'X.OX.OXOX', 'XOXXX.OOO', 'X..OXOOXX', '...XXX.OO', 'XXOOX..XO', '..XOXOX..', 'OX.XXXO.O', '.X.OXO.X.', '.XXOX.OXO', 'XXXOXO..O', 'XXO.XXOOO', '.XOXOOXXO', 'X.XOOOXXO', 'XX.OXO.XO', 'XX.X..OOO', 'O.XXOX.OX', 'XOXX..XOO', '.OO...XXX', 'XX.X.OXOO', 'X...XO.OX', '.XXOOXO.X', 'OXX.XOX.O', 'X.XOOOX..', 'OOXXXOXOX', 'OOX.X.XOX', '.XXOOO..X', 'OXXOX.O..', 'OX.XXOOX.', 'X.OO.OXXX', 'OXXXXOOOX', '.XOXXO..O', '.XOOXOXX.', '.OXXOOXOX', 'X.O.OOXXX', 'O.X..X.OX', 'O.XO.X..X', 'XO..OXXO.', 'XXOX.OOXO', 'OOOXX.XXO', 'XXXO..O..', '.XOXOXOOX', 'XXOXOOX..', 'O.XO.XOX.', 'X.O.XO.XO', 'XXXO.O...', 'X..XXOOOX', 'OXOXOXXOX', 'X.X..XOOO', 'O.X.OX.XO', '.XX.X.OOO', 'XOOXX.X.O', 'OXOXXXO..', '.OXO.X..X', 'OOXX.X.OX', 'OOOOXXXX.', 'O.X.XOXXO', 'OXOXOXX.O', 'O.OOXXOXX', 'XXOXXOO.O', 'XO..X..OX', 'XX..X.OOO', 'XO.OXO.XX', '.OXXOXO.X', 'XOOXXXO..', 'XOOOXXXXO', 'OX.OOXOXX', '..XOOOXX.', 'OOXOX.OXX', 'XXXX.O.OO', 'XOOXXXXOO', '..XXX.OOO', 'XXO.OOOXX', 'OX..O.XXO', 'XO.OX...X', 'XXXOX.OO.', 'X.OXO.O.X', 'X.XXOXOOO', '..OXXXOOX', 'XOOXOOXXX', 'XO.OO.XXX', 'XXXOXOOOX', 'O.XOOXX.X', '.OX.XOXOX', 'OXXO.XOXO', 'XOOOX.X.X', 'OXOOOXXXX', 'XXXOO.OX.', 'X..XO.XO.', 'OOO.XX..X', 'XOO.XO.XX', 'OXXOXOX..', 'OXOXX.OX.', 'O..OX.OXX', '.OXOX.X..', '.X..XXOOO', 'X.XX..OOO', 'XOXX.OXO.', 'OXXOOOXX.', 'OOX.XXO.X', 'X.X.XOXOO', 'OXOXXXOXO', 'XXOOOO.XX', 'OX.XX.OXO', 'XOX.XOO.X', 'OOXO.X.XX', 'XXXOO..XO', 'OO.XXXX.O', 'O.XO.OXXX', 'XO..XOXOX', '.OX.X.XO.', '.XO.X.OX.', 'XOOXOXO.X', '.OOXXX.OX', 'OOOX..XX.', 'XX.OOOOXX', 'OX.OO.XXX', '.XO.OOXXX', 'XOOXO.XX.', '..OXOOXXX', 'XOO.XXO.X', 'XOX.XXOOO', 'X..XOOX..', 'XO.XXX.OO', '..X.X.XOO', 'OXXO.XO..', 'XOO.OXOXX', 'XO.XOX.O.', 'X.XOOXO.X', 'XXXXOOO..', '.OXO.XXOX', 'OXX.X.XOO', 'X.XOOO.X.', 'O.XXXOX.O', 'X.OXOOXX.', 'OX.XOXXOO', 'XX.XO.XOO', '.XOOX.XXO', '.OOXOXOXX', '.XXOOO.X.', 'OOX.XOXX.', '.OX.OX..X', 'OOOXXOXX.', 'OOX.O.XXX', 'XOOOXXXOX', 'XXO.O.OX.', 'XXX..OXOO', 'OOXXXOOXX', 'OO.X.OXXX', 'OOO..X.XX', 'OOXXXXOOX', 'XXOXXOOOX', '..XOXXOOX', 'XXXOX.O.O', 'OXOO.XOXX', 'XO.X.OXXO', 'XOX.O..OX', 'XXXO.O.XO', 'XX.XOOXO.', 'XXOXOOOX.', 'XXOOXOX.O', 'OOXXXOXXO', 'OOX.XX.OX', 'XOOXXX..O', 'XOXOOXOXX', 'OOOXX..X.', 'XXXXOOOOX', '.OXOX.XOX', 'OOOOXX.XX', '.O.OXOXXX', 'OX..XXOXO', 'XO.X..XO.', 'XOXXOOXXO', 'O.XXXXO.O', '.OXX.XOOX', 'OXXXX.OOO', 'XXOXOXXOO', 'OOXOXXXXO', 'O.X.OXX.O', 'OOOX...XX', '.OOXXXO.X', '...OO.XXX', 'OO.XOXXOX', '.OXOXXX.O', 'XOXO.XO.X', 'XXXO.OXO.', 'O..XOXX.O', 'XO..XO..X', 'XO..O.XOX', 'O.X.X.XO.', 'XOOXXOXOX', 'OXXO.X.OX', 'X.OXXO.OX', 'XXXX.OO.O', 'O..O.XOXX', 'OXXXOX.OO', 'OOXO.XX.X', 'OOX.OXX.X', 'XXX..O.O.', 'XOOXXO..X', 'OXX.X.OXO', 'OX..OX.XO', '.XXOOOOXX', 'O..XXX.O.', 'XX.XOOX.O', '..OOXOXXX', '..XX.XOOO', 'OX.OXXO..', '.X.X.XOOO', 'X.XOOOOXX', 'X.O.XXOOX', 'X.O.X.O.X', 'XOOXXXOXO', '.OOO.XXXX', '..XXOXOOX', 'XXX.OO.OX', 'OO.XXX.XO', 'O..OOXXXX', 'OXXOOX..X', '..XOOOX.X', '.O.XXXOXO', '.X.OXOXXO', '.XX.XOXOO', 'XXXO.XO.O', 'X.OOX.XOX', 'OXOX.OXXO', 'OXO.O.XXX', 'OX..X.OX.', 'O.XOOXXXO', '..OXO.OXX', '.XXX..OOO', 'X..X.OXO.', 'X.OXX.OOX', 'O.XXXX.OO', 'OXXXO...O', 'XXOOOXXXO', 'XOOX..X..', '.XXXOXOOO', 'OXXXXOXOO', 'OO.O.XXXX', 'X.XX.OXOO', 'XO.XO..OX', 'OOXXXOX..', 'OXO.XOXX.', '.OXXXOXO.', 'OXXXOOX.O', 'O.OO.XXXX', 'X.OXXO..O', 'XOO..OXXX', 'XXX.O.XOO', 'X.XXXOOOO', 'X...X.OOX', 'OXOXXX.O.', 'OOX.X.X..', 'XO.OXX.OX', 'XXX.OXO.O', 'OXX..XOOX', 'OOO.XX.X.', 'OO.OXXOXX', 'X..XOOXOX', 'XOXOXXXOO', '.OXO.XOXX', 'XX...XOOO', 'XXOXXO.OO', 'XOOXXOX..', 'XOXXXOOOX', '..OXXXOXO', 'XX.OOO.X.', '..O.OXOXX', 'O.XOX.XXO', 'O.XOO.XXX', 'XXX.OOX.O', 'OXOXOXOX.', 'OXOXXOX.O', '.O.XXX..O', 'OOOX.X..X', 'XO.XO.XXO', 'OOX.X.XXO', 'OXXOX.XO.', '.O.XXX.O.', 'XXOXO.OXO', 'XOOOXXOXX', 'X..OOOXX.', 'OXXO..O.X', 'OOO.X.XX.', 'O.OXXXXO.', 'XXXOXOXOO', 'OOOX.XOXX', 'OOOX.XX..', 'XO.XOXX.O', 'XX.OX.OOX', 'XOXOOXXXO', 'XO..OOXXX', 'OXOXXO.X.', 'O.X.XOX..', '..XO.X.OX', 'XOXXOOX..', 'XOX.OX.O.', 'OXXXOO.XO', 'XOOXX.XO.', 'XX.XXOOOO', '.XOOX.OXX', 'XOXXOOOXX', 'O.O...XXX', '..XOOX..X', '.O.XO.XOX', 'O..OXXOX.', 'OXXOXOO.X', 'XOOXO.OXX', '.OOXXXOX.', 'OXXX.XOOO', 'OXXOOXX.O', 'X.XOXOXO.', 'XXO.XO.OX', 'X.O.X..OX', 'OXX.XXOOO', 'OXOOX..XX', 'XO.X.OX..', 'O...OXXXO', 'XOX..XOOX', 'XXO.XOXOO', 'OOO..XX.X', 'XXOXO.OOX', '.XO.OXO.X', 'XOXOXOOXX', 'OX.XOOXXO', '.XO.XOOXX', 'XOO.O.XXX', 'O.OXOXXXO', 'XO.X.XXOO', 'OXXOXO.X.', 'XO..XOOXX', 'O.X..XO.X', '.OX.OOXXX', 'OOO.XXXOX', 'XO..OX.OX', 'XO.X..X.O', '.XXOXO.XO', 'XXO.XOO.X', 'OXX.OX.OX', '.XXOOOX..', '.OXXOXXOO', 'X.OXO.OX.', 'XXOOXOXOX', 'O.X.OXOXX', 'OOOX.XXOX', 'XXOOXOOXX', 'OXXOOXOX.', 'XXXXOO..O', 'O.X.OXXOX', 'OOOOXXX.X', 'XXOX.OXO.', 'XOXXOX.OO', 'XXX.O.O..', 'O.OXO.XXX', 'XO.XXO.OX', 'O.XX.XOOX', 'O.XXOXXOO', 'OXOOXXXOX', 'O..O..XXX', 'OO.OX.XXX', '....OOXXX', 'XXO.OXOXO', '.XO.XOX.O', 'XXOOOOXX.', 'X..OX..OX', 'XO..X.O.X', 'XOXXXOXOO', 'XOXOXOX..', 'OXX.O.X.O', 'XXXOOX.O.', 'X..OOOX.X', 'XXOOOXXOX', 'O.XXX.XOO', 'OXXOXOXOX', '..OXXOX.O', 'XXOOOOX.X', 'OX.OXXOOX', 'X.OXXX.OO', 'OXOXXOOXX', 'X.OXXOO.X', 'X..OXO..X', 'O.X.XXXOO', 'OXOXXX..O', '.OX.XOX..', 'OOXXOOXXX', 'XXX..OOXO', 'X.X.XOOOX', '.O.XXXO..', 'OX..OXX.O', 'OOXOXX..X', 'XOOX.XXO.', 'XO.X.OXOX', '.OXXXX.OO', '.XX.OXOOX', 'XXXO.OO.X', '.XO.XO.X.', 'OOXXOX.XO', '.OOXXX...', 'X..XOXXOO', 'XOXOOXXO.', 'X.OXXOOXO', 'OOOXOXXX.', 'XO.OOXXOX', 'OXOOX.XX.', '.XXOOOXXO', '.OO.XOXXX', 'OXXXO.XOO', 'XX.OX.OXO', '.O.XXXXOO', 'XXXO..XOO', 'XXX.OX.OO', 'OOOXX.OXX', 'X.OOXO.XX', 'X.O.XOX.O', '.XOXO.O.X', '.XOX.O.XO', 'OO.XXX...', 'X.OXXXO.O', 'OOO.XXXXO', 'OXXXOXOOX', 'XXXO.OX.O', 'O.X.XXOOX', '.OX.XXOOX', '.O.OOXXXX', 'XOOOOXXXX', 'OO.XXXXO.', '..OXXXO..', '..OXOXO.X', 'OX..XO.X.', 'OXX.OXOXO', 'X.OXOXOXO', 'XO.XXOO.X', '.XO.OXOX.', 'OX.XO.X.O', '.OXOXXXO.', '.OXOXOXX.', 'O..XXXXOO', 'XOXXO..O.', 'X.OX.O.XO', 'OOO.XXX..', 'OO..OXXXX', 'OX.OX.XXO', 'XXXXO.OO.', '..X.XOX.O', 'OOO.X.X.X', 'XOXOX..OX', 'OXXOO.XXO', 'XXO..OX.O', 'OX.XO..XO', 'XXO.O.O.X', 'XXXOO....', 'XXOXOO.XO', 'XXX.OOO.X', '..OXXXXOO', 'OXO.X.OXX', 'XOO.XOX.X', 'O.OX.OXXX', 'X..OX.O.X', 'O...O.XXX', 'O..XOX.XO', 'XXXO.XOO.', 'XXOXO.X.O', 'XXX.XOOO.', '..XOX.XO.', 'OOXXOX..X', 'XX..XOOXO', 'OXX.XOOX.', 'OOX..X..X', 'XO.XXXOO.', 'XOXOXXOOX', 'O.XOXXX.O', 'XXX..O..O', 'OOXO..XXX', 'OO....XXX', 'XXXOOXOOX', 'X..X..XOO', '..XO.XO.X', 'XOXXO.X.O', 'O.XOXOOXX', 'OX..XOXXO', '.XOXOXO..', '.O.O..XXX', 'XXX.O.OXO', 'OOO.XXOXX', 'XO.XOOX.X', 'XOXOX.O.X', '.OO.OXXXX', 'XXX.OOXO.', '.X.OX.OX.', '.XXOOOXOX', '.OOX.OXXX', 'OOX.XOX.X', 'OX.O.XOX.', 'O.XOX.OX.', 'XXOOX.OX.'}
inputs = input()
while len(inputs) != 3:
    print('valid' if inputs in answer_set else 'invalid')
    inputs = input()