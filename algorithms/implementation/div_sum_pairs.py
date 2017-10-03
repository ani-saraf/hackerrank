import sys

def divisibleSumPairs(n, k, ar):
    nums = [0] * k
    count = 0
    for ele in ar:
        modu = ele % k
        count += nums[(k - modu) % k]
        nums[modu] += 1
    return count

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)