# https://www.codewars.com/kata/human-readable-time/

def make_readable(seconds):
    intervals = [
        60 * 60,
        60,
        1,
    ]

    result = []
    for interval in intervals:
        q, seconds = divmod(seconds, interval)
        result.append(q)

    return '{:02d}:{:02d}:{:02d}'.format(*result)
