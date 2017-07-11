import numpy
m, n = map(int, input().split())
a = [input().strip().split(' ') for _ in range(m)]
np_array = numpy.array(a, int)
print(np_array.transpose())
print(np_array.flatten())