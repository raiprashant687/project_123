import numpy

s1 = []
s = list(map(int, input().split()))
for i in range(s[0]):
    s1.append(list(map(int, input().split())))

mynewarray = numpy.array(s1)
print(numpy.mean(mynewarray, axis=1))
print(numpy.var(mynewarray, axis=0))
result = round(float(numpy.std(mynewarray)),11)
print(result)
