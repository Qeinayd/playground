# https://www.codewars.com/kata/highest-and-lowest/

def high_and_low(numbers):
    numbers = [int(x) for x in numbers.split(' ')]
    return ' '.join(str(x) for x in [max(numbers), min(numbers)])
