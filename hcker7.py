#!/bin/python3

import math

t = int(input())

if t > math.pow(10, 5):
    print("exceeded")
else:
    for _ in range(t):
        n = int(input())
        if n > math.pow(10, 9):
            break
        sum1 = 0
        for j in range(n):
            if j % 3 == 0 or j % 5 == 0:
                sum1 = sum1 + j
        print(sum1)





