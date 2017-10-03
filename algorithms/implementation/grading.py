grades = [int(input()) for _ in range(int(input()))]
[print(g+5 - g%5 if g%5 > 2 and g>37 else g) for g in grades]
