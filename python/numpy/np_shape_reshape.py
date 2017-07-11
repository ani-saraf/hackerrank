import numpy
a = input().strip().split(' ')
np_array = numpy.array(a, int)
print(numpy.reshape(np_array,(3,3)))
