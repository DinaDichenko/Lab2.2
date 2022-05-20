#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    for i in range(10, 100):
        if (i % (i % 10 + i // 10)) == 0:
            print(i)
