import random
import numpy

with open("data.txt", 'w') as f:
    arr = numpy.array([(random.randint(i, 1000), random.randint(1, 1000 * (1000 - i))/100) for i in range(1000)])
    for datapoint in arr:
        print("{a} {b}".format(a=datapoint[0], b=datapoint[1]), end="\n", file=f)
