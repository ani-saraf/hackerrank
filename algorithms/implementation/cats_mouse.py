for _ in range(int(input().strip())):
    a,b,c = map(int, input().strip().split(' '))
    dist_a = abs(c - a)
    dist_b = abs(c - b)
    print('Cat A' if dist_a < dist_b else 'Cat B' if dist_a > dist_b else 'Mouse C')