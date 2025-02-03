from collections import deque
from decimal import Decimal, getcontext, ROUND_HALF_UP


def maxAvgSubArray(nums, k):
    def add5Prec(a, b):

        getcontext().prec = 20  # Set high working precision
        getcontext().rounding = ROUND_HALF_UP  # Standard rounding

        a = Decimal(a)
        b = Decimal(b)
        result = (a / b).quantize(Decimal("0.00000"))
        return result

    dq = deque(maxlen=k)
    max_avg, total, avg = [0, 0, 0]

    if k == len(nums):
        import math

        return add5Prec(math.fsum(nums), k)

    for i in range(k):
        dq.append(nums[i])

    total = sum(dq)
    max_avg = add5Prec(total, k)
    dq_full = True

    for i in range(k, len(nums)):
        dq.append(nums[i])
        total = sum(dq)
        avg = add5Prec(total, k)
        if avg > max_avg:
            max_avg = avg

    return max_avg


nums = [8, 0, 1, 7, 8, 6, 5, 5, 6, 7]
k = 5
print(maxAvgSubArray(nums, k))
