# https://www.codewars.com/kata/string-incrementer/

def increment_string(strng):
    if not strng:
        return '1'

    n = []
    for char in strng[::-1]:
        if char.isdigit():
            n.append(char)
        else:
            break
        
    n_len = len(n)
    n = int(''.join(n[::-1])) if n else 0

    return strng[:len(strng) - n_len] + str(n+1).zfill(n_len)
