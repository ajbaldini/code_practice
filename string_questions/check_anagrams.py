"""
How do you check if two strings are anagrams of each other?
"""

def check_anagram(wordOne, wordTwo):
    one = list(wordOne)
    two = list(wordTwo)
    one.sort()
    two.sort()

    if one == two:
        print(''.join(wordOne) + " and " + ''.join(wordTwo) + " are anagrams")
    else:
        print(''.join(wordOne) + " and " + ''.join(wordTwo) + " are not anagrams")

print(check_anagram('listen','silent'))
print(check_anagram('listens', 'silent'))

