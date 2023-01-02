"""
Check to see if a string has the same amount of 'x's and 'o's.
The method must return a boolean and be case insensitive. The string can contain any char.
"""
def xo(s):
    count = 0
    for i in s.upper():
        if i == 'X':
            count += 1
        elif i == 'O':
            count -= 1
    return True if count == 0 else False

print(xo('xooxXO'))