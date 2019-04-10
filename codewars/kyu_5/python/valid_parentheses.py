# https://www.codewars.com/kata/valid-parentheses/

def valid_parentheses(string):
    brackets = {
        '(': ')',
    }
    stack = []

    for char in string:
        if char in brackets:
            stack.append(char)
        else:
            if char in brackets.values():
                if len(stack) and brackets[stack[-1]] == char:
                    stack.pop()
                else:
                    return False

    return not len(stack)
