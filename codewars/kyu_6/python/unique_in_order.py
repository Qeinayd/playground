# https://www.codewars.com/kata/unique-in-order/

def unique_in_order(iterable):
    if not iterable:
        return []
    if len(iterable) < 2:
        return list(iterable)
    
    result = [iterable[0]]
    for x in iterable[1:]:
        if result[-1] != x:
            result.append(x)
            
    return result
