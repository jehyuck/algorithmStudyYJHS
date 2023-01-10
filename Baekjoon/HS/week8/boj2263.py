import sys
sys.setrecursionlimit(10**5)

input = sys.stdin.readline

n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))
pre_order = []

in_order_idx = [0] * (n + 1)

for i in range(n):
    in_order_num = in_order[i]
    in_order_idx[in_order_num] = i


def make_pre_order(in_start, in_end, post_start, post_end):
    if (in_start > in_end) or (post_start > post_end):
        return

    parent = post_order[post_end]
    pre_order.append(parent)

    left_child = in_order_idx[parent] - in_start
    right_child = in_end - in_order_idx[parent]

    make_pre_order(in_start, in_start + left_child - 1, post_start, post_start + left_child - 1)
    make_pre_order(in_end - right_child + 1, in_end, post_end - right_child, post_end - 1)


make_pre_order(0, n - 1, 0, n - 1)

print(*pre_order)