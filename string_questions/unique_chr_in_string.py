"""
Given a string input, determine if each character is unique, do not use any other data structures
"""

def isStringUnique(s):
    cnt = 0
    s = s.lower()

    for c in s:
        for l in s:
            if c == l:
                cnt += 1

    if cnt > len(s):
        return "NO"
    else:
        return "YES"

print(isStringUnique("abcde")) #YES
print(isStringUnique("abccde")) #NO
print(isStringUnique(("aabbccde"))) #NO