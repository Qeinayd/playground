# https://www.codewars.com/kata/find-the-odd-int/

def find_it(seq):
    for value in seq:
        if seq.count(value) % 2 == 1:
            return value
