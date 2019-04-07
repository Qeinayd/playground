# https://www.codewars.com/kata/vowel-count/

def getCount(inputStr):
    num_vowels = 0
    for char in inputStr:
        if char.lower() in 'aeiou':
            num_vowels += 1
    return num_vowels
