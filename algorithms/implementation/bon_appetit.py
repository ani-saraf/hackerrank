def bonAppetit(n, k, b, ar):
    return "Bon Appetit" if b == (sum(ar)-ar[k])/2 else int(b-((sum(ar)-ar[k])/2))

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)