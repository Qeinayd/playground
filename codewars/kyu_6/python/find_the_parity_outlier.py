# https://www.codewars.com/kata/find-the-parity-outlier/

def find_outlier(integers):
    signs = [bool(x % 2) for x in integers[:3]]
    entirely_odd = True if signs.count(True) > signs.count(False) else False
    
    for x in integers:
        if entirely_odd and not x % 2:
            return x
        if not entirely_odd and x % 2:
            return x
