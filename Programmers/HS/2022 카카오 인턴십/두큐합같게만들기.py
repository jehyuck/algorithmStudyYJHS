from collections import deque


def solution(queue1, queue2):
    # 큐
    q1 = deque(queue1)
    q2 = deque(queue2)

    # 최대 작업 횟수
    limit = len(queue1) * 4

    # 각 큐에 있는 수의 합
    sum1 = sum(queue1)
    sum2 = sum(queue2)

    # 두 큐의 총합이 홀수인 경우
    if (sum1 + sum2) % 2:
        return -1

    # 작업 횟수
    count = 0

    # 두 큐의 총합이 같을 때까지 반복
    while sum1 != sum2:
        # 작업 횟수가 최대 작업 횟수를 초과한 경우
        if count == limit:
            # 각 큐의 원소 합을 같게 만들 수 없음.
            return -1

        # 작업 횟수 추가
        count += 1

        # q1에 들어있는 수의 합이 더 큰 경우
        if sum1 > sum2:
            # q1에서 원소 추출
            val = q1.popleft()
            # 추출한 원소 q2에 삽입
            q2.append(val)
            # sum1, sum2 갱신
            sum1 -= val
            sum2 += val
        # q2에 들어있는 수의 합이 더 큰 경우
        else:
            # q2에서 원소 추출
            val = q2.popleft()
            # 추출한 원소 q1에 삽입
            # sum1, sum2 갱신
            q1.append(val)
            sum1 += val
            sum2 -= val

    # 작업 횟수 반환
    return count


# 입출력 예
queue1 = [3, 2, 2]
queue2 = [1, 1, 1]
result = 2

print(result == solution(queue1, queue2))

