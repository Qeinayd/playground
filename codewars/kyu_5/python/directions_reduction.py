# https://www.codewars.com/kata/directions-reduction/

def dirReduc(arr):
    opposition = {
        'NORTH': 'SOUTH',
        'SOUTH': 'NORTH',
        'EAST': 'WEST',
        'WEST': 'EAST'
    }

    idx = 0
    while idx < len(arr) - 1:
        if opposition[arr[idx]] == arr[idx + 1]:
            arr.pop(idx)
            arr.pop(idx)
            if idx:
                idx -= 1
        else:
            idx += 1
    
    return arr
