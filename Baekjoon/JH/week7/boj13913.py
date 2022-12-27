from collections import deque as dd

s, d = map(int, input().split())
visitDict = dict()


def solution(start, target):
    if start > target:
        return start - target

    que = dd()
    answer = 0

    visitDict[start] = -1
    crt = start
    que.append(crt)
    while crt != target and que:
        temp = []
        for j in que:
            crt = j
            go = [crt-1, crt + 1, crt * 2]
            if crt == target:
                break
            if go[0] >= 0:
                if go[0] not in visitDict:
                    visitDict[go[0]] = crt
                    temp.append(go[0])

            for i in range(1, 3):
                if go[i] > 200000:
                    continue
                if go[i] not in visitDict:
                    visitDict[go[i]] = crt
                    temp.append(go[i])
        if crt == target:
            break
        answer += 1
        que = temp

    return answer


print(solution(s, d))

answerQue = dd()
answerQue.append(d)
crt = d
if crt in visitDict:
    while visitDict[crt] != -1:
        crt = visitDict[crt]
        answerQue.appendleft(crt)
else:
    answerQue = range(s, d-1, -1)
print(*answerQue)





