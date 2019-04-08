# https://www.codewars.com/kata/multiples-of-3-or-5/

def solution(number):
    result = []
    for x in range(number):
        if x % 3 == 0 or x % 5 == 0:
            result.append(x)
    return sum(result)
