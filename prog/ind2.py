#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cmath
import sys

if __name__ == '__main__':
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    dis = pow(b, 2) - 4*a*c

    if dis < 0:
        print("there are no roots")
    elif dis == 0:
        x = cmath.sqrt((-b)/2*a)
        print("x1 = ", x, "x2 = ", -x)
    elif dis > 0:
        x1 = cmath.sqrt(((-b-cmath.sqrt(dis)) / (2 * a)))
        x2 = cmath.sqrt(((-b+cmath.sqrt(dis)) / (2 * a)))
        print("x1 = ", x1, "x2 = ", -x1, "x3 = ", x2, "x4 = ", -x2)
    else:
        print("Error")
