# https://www.codewars.com/kata/consecutive-strings/

def longest_consec(strarr, k):
    if len(strarr) == 0:
        return ''
    if k > len(strarr):
        return ''
    if k <= 0:
        return ''
    return max([''.join(strarr[i:i+k]) for i in range(len(strarr))], key=len)
