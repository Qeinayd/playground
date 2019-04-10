# https://www.codewars.com/kata/simple-pig-latin/

def pig_it(text):
    return ' '.join(
        word[1:] + word[0] + 'ay'
        if all(x.isalpha() for x in word)
        else word
        for word in text.split(' ')
    )
