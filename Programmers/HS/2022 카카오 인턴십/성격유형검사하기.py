def solution(survey, choices):
    answer = ""
    # 성격 유형 지표
    types = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]
    # 성격 유형 점수
    scores = {
        'R': 0,
        'T': 0,
        'C': 0,
        'F': 0,
        'J': 0,
        'M': 0,
        'A': 0,
        'N': 0,
    }

    # 검사 질문, 점수
    for s, c in zip(survey, choices):
        # 동의인 경우
        if c - 4 > 0:
            # 동의 관련 성격 유형 점수 추가
            scores[s[1]] += c - 4
        # 비동의인 경우
        else:
            # 비동의 관련 성격 유형 점수 추가
            scores[s[0]] += 4 - c

    # 성격 유형 지표
    for type in types:
        # 점수가 높은 유형을 정답 문자열에 추가
        if scores[type[0]] >= scores[type[1]]:
            answer += type[0]
        else:
            answer += type[1]

    return answer


# 입출력 예
survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
result = "TCMA"

print(result == solution(survey, choices))