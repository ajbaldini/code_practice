"""
How do you check if two strings are anagrams of each other?
"""

def check_anagram(wordOne, wordTwo):
    one = list(wordOne)
    two = list(wordTwo)
    one.sort()
    two.sort()

    if len(one) != len(two):
        return False

    x=0
    for i in one:
        if i != two[x]:
            return False
        x=x+1
    return True

wordOne = 'listen'
wordTwo = 'silent'

isAna = check_anagram(wordOne,wordTwo)
if isAna:
    print(wordTwo + " and " + wordOne + " are anagrams")
else:
    print(wordTwo + " and " + wordOne + " are not anagrams")