def solution(cap, n, deliveries, pickups):
    answer = 0

    del_end = n - 1
    pi_end = n - 1
    del_count = cap
    pi_count = cap

    # 끝에서 부터 배달을 마친다는 생각으로 상자갯수를 줄여 나간다.
    while del_end != -1 or pi_end != -1:

        # 가장 끝 부분을 가장 먼 곳을 구하기 전에 당겨준다.
        while pi_end != -1:
            if pickups[pi_end] == 0:
                pi_end -= 1
            else:
                break
        while del_end != -1:
            if deliveries[del_end] == 0:
                del_end -= 1
            else:
                break

        # 픽업과 배달중 더 먼곳을 구한다.
        dist = max(del_end, pi_end) + 1

        # 배달 하기
        while del_count > 0 and del_end >= 0:
            # print(del_end, del_count)
            if deliveries[del_end] <= del_count:
                del_count -= deliveries[del_end]
                deliveries[del_end] = 0
                del_end -= 1
            elif deliveries[del_end] > del_count:
                deliveries[del_end] -= del_count
                break

        # 똑같은 방법으로 픽업 상자를 계산
        while pi_count > 0 and pi_end >= 0:
            # print(pi_end, pi_count)
            if pickups[pi_end] <= pi_count:
                pi_count -= pickups[pi_end]
                pickups[pi_end] = 0
                pi_end -= 1
            elif pickups[pi_end] > pi_count:
                pickups[pi_end] -= pi_count
                break

        # 왕복비용으로 2를 곱한 값을 구한다.
        answer += dist * 2

        # 택배 상자를 비워주는 코드
        del_count = cap
        pi_count = cap
    return answer

print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
print(solution(	2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))
print(solution(2, 2, [0,6], [0,0]))
print(solution(2, 2, [1,0], [1,0]))