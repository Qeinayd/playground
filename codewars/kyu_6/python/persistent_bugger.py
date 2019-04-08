# https://www.codewars.com/kata/persistent-bugger/
import functools
import operator


def persistence(n):
    counter = 0
    while n > 10:
        n = int(functools.reduce(operator.mul, [int(x) for x in str(n)], 1))
        counter += 1
    return counter
