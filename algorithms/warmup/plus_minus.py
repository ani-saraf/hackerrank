n = float(input())
arr = [int(x) for x in input().split()]

print(format(len([x for x in arr if x > 0])/n, ".6f"))
print(format(len([x for x in arr if x < 0])/n, ".6f"))
print(format(len([x for x in arr if x == 0])/n, ".6f"))