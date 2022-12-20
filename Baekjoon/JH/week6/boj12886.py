from collections import deque as d

# 돌 입력 받는다
A, B, C = sorted(map(int, input().split()))


# tuple로 set에 저장하면 공간이 낭비 될까봐 int로 변환해서 저장한다.
def gethash(arr):
    return arr[0] * fir + arr[1] * sec + arr[2]



# 자릿수에 따른 해쉬 계산값
fir = 500 * 500
sec = 500

# visit을 set으로 관리한다
visitSet = set()
# que bfs를 통해 모든 경우를 탐색한다.
que = d()

# 처음상태를 집어넣는다.
que.appendleft((A, B, C))
# 초기엔 답을 구한 상태가 아니므로 0으로 만든다
answer = 0


# 처음 상태가 정답이라면 이를 처리한다.
if A == B == C:
    que.popleft()
    answer = 1


# 정답이 나올 때까지 반복문을 진행시킨다.
while que and not answer:
    A, B, C = que.popleft()

    # 정렬된 list들 중에서 que앞에 부분걸 가져와서
    # 문제에 나온 연산대로 X = x+x Y = y-x를 모든 경우의 수 3가지로 구한다
    tA = A + A
    tB = B - A
    tC = C - A

    # 정답이 나올수 있는 경우의 수는 a와 c를 계산 연산 했을 때 뿐이다.
    if tA == B == tC:
        answer = 1
        break

    # 리스트를 a에 x연산을 했을때 기준으로 2가지를 먼저 구한다.
    tList1 = sorted([tA, tB, C]) # 1경우 리스트 정렬
    t1Hash = gethash(tList1)     # 1경우 해쉬 구함
    tList2 = sorted([tA, B, tC]) # 2경우 리스트 정렬
    t2Hash = gethash(tList2)     # 2경우 해쉬

    # 해쉬가 set에 존재하지 않는다면 visit 처리 후 que에 이 상태를 저장
    if t1Hash not in visitSet:
        que.append(tList1)
        visitSet.add(t1Hash)
    if t2Hash not in visitSet:
        que.append(tList2)
        visitSet.add(t2Hash)

    # b = x, c = y인 경우에 계산 연산을 해준다.
    ttB = B + B
    ttC = C - B

    tList3 = sorted([A,ttB,ttC])
    t3Hash = gethash(tList3)
    # b와 c가 각각 x, y인 경우는 연산 후 정답이 될 수 없다.
    if t3Hash not in visitSet:
        que.append(tList3)
        visitSet.add(t3Hash)

print(answer)