import numpy as np
n = input()
A = np.array([input().split() for _ in range(int(n))], int)
B = np.array([input().split() for _ in range(int(n))], int)
print(np.dot(A,B))
