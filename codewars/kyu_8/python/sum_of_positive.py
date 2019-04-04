# https://www.codewars.com/kata/sum-of-positive/

def positive_sum(arr):
    if not arr:
        return 0
    
    return sum(filter(lambda x: x >= 0, arr))
