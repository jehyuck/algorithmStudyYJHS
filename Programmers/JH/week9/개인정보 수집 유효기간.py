def solution(today, terms, privacies):
    answer = []

    # 오늘을 분리해서 저장한다.
    # 약관을 dict로 관리한다.
    today = list(map(int, today.split('.')))
    today[1] -= 1
    term = dict()

    for i in terms:
        a, b = i.split(' ')
        term[a] = int(b)
    # print(*today, sep='.')
    # 모든 개인 정보에 대해 보관기간을 구하고 모든 것을 비교한다.
    for i in range(len(privacies)):
        privacy = privacies[i]

        p_day, p_term = privacy.split(' ')
        end_day = list(map(int, p_day.split('.')))

        end_day[1] += term[p_term] - 1
        a, b = divmod(end_day[1], 12)

        end_day[0] += a
        end_day[1] = b

        # print(*end_day, sep=".")
        # 년도가 이미 지났으면
        if end_day[0] < today[0]:
            answer.append(i + 1)
        # 년도가 동일하면
        elif end_day[0] == today[0]:
            # 달이 이미 지났으면
            if end_day[1] < today[1]:
                answer.append(i + 1)
            # 달이 동일하면
            elif end_day[1] == today[1]:
                # 일수가 지났으면
                if end_day[2] <= today[2]:
                    answer.append(i + 1)

    return answer