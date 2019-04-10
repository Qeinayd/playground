# https://www.codewars.com/kata/moving-zeros-to-the-end/

def move_zeros(array):
    idx = len(array) - 1

    while idx >= 0:
        if array[idx] == 0 and array[idx] is not False:
            array.append(array.pop(idx))
        idx -= 1

    return array
