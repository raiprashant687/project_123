import numpy

N = input()
s = []
r = []
for i in range(int(N)):
    s.append(list(map(int, input().split())))
for j in range(int(N)):
    r.append(list(map(int, input().split())))

mynewarray1 = numpy.array(s)
mynewarray2 = numpy.array(r)

print(numpy.dot(mynewarray1, mynewarray2))


