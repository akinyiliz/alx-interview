#!/usr/bin/python3
'''Minimum Operations challenge'''


def minOperations(n):
    if n <= 0:
        return 0

    operations = 0
    i = 2
    while i <= n:
        operations += 1
        if i * 2 > n:
            break
        i *= 2

    return operations + minOperations(n - i)
