def migratoryBirds(n, ar):
    return -max((ar.count(i), -int(i)) for i in set(ar))[1]

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)