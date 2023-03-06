from collections import defaultdict as dd
import math as m
import bisect

# 입력
N, B = map(int, input().split())
nums_dict = dd(int)

for i in map(int, input().split()):
    nums_dict[i] += 1


# 등장한 성능을 정렬
keys = list(nums_dict.keys())
keys.sort()
answer = keys[0]
a = 0
mid = 0
last_a = 2000000000
# (?(최대 key[i+1}) - key[i])^2 * numdic[i] 의 합을 구하는 문제
# dp로 가능한가?


def calc_B(key, target):
    return ((target - key) ** 2) * nums_dict[key]


answer = a
while a <= last_a:
    mid = (a + last_a) // 2
    idx = bisect.bisect_right(keys, mid)
    find_bool = True
    temp = 0
    for i in range(idx):
        temp += calc_B(keys[i], mid)
        # print(temp <= B, idx, a, last_a, keys, mid, B)
        if temp <= B:
            continue
        else:
            find_bool = False
            break
    if find_bool:
        # print(idx, a, last_a, keys, mid)
        answer = mid
        a = mid + 1
    else:
        last_a = mid - 1
# print(nums_dict)

print(answer)