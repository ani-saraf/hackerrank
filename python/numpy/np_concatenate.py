import numpy as np
m, n, p = map(int,input().split())
arrA = np.array([input().split() for _ in range(m)],int)
arrB = np.array([input().split() for _ in range(n)],int)
print(np.concatenate((arrA, arrB), axis = 0))