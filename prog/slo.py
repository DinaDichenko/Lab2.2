#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import sys

if __name__ == '__main__':
    eps = 1e-10
    k = 0
    n = int(input("Enter n: "))
    x = float(input("Enter x: "))

    s = 0
    a = 1/math.factorial(n)
    while abs(a) > eps:
        s += a
        k += 1
        a = pow((-pow(x, 2)) / 4, k)/(math.factorial(k) * math.factorial(n + k))

    Ix = pow((x / 2), n) * a
    print("The Bessel function of the first kind =", Ix)
