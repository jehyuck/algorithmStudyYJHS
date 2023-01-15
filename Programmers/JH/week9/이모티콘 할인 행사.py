import math


def solution(users, emoticons):
    # 전부다 구한다.
    case = []
    dfs([0, 0, 0, 0], case, emoticons, 0, [6, 7, 8, 9])
    # print(case)

    answer = [0, 0]
    # 모든 경우를 전부 찾은 값으로 답을 찾는다.
    for i in case:
        temp = [0, 0]

        # 매번마다 합을 구하면 낭비이기 때문에 누적합을 구해놓는다.
        for j in range(1, 4):
            i[j] += i[j - 1]

        # 한경우에 모든 유저를 탐색해 답을 구한다.
        for dis, margin in users:

            # 그 유저의 할인값이 어떻게 되어야 하는지를 구한다.
            j = 4 - math.ceil(dis / 10)

            # 해당 비용이 유저의 마진보다 작은경우
            if margin > i[j]:
                temp[1] += i[j]
            # 해당 비용이 유저의 마진보다 작거나 같은경우
            else:
                temp[0] += 1

        # 답을 플러스 이용자수, 그다음 매출액을 통해 최선값을 구한다.
        if temp[0] > answer[0]:
            answer = temp
        elif temp[0] == answer[0] and temp[1] > answer[1]:
            answer = temp

    return answer


def dfs(crt, case, emoticons, depth, discounts):
    if len(emoticons) == depth:
        case.append(crt)
        return

    for i in range(4):
        temp = crt.copy()
        temp[i] += emoticons[depth] * discounts[i] // 10
        dfs(temp, case, emoticons, depth + 1, discounts)