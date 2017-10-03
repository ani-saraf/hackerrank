def sockMerchant(n, ar):
    return sum(ar.count(x) // 2 for x in set(ar))

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)