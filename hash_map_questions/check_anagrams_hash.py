def check_anagram(wordOne, wordTwo):
    wordOne = wordOne
    wordTwo = wordTwo
    n = 0
    word_h = {}

    if len(wordTwo) != len(wordOne):
        print(f"{wordOne} and {wordTwo} are not anagrams")
        return

    for i in wordOne:
        word_h.setdefault(i, 0)
        word_h[i] += 1

    for i in wordTwo:
        if i in word_h:
            word_h[i] -= 1
        else:
            print(f"{wordOne} and {wordTwo} are not anagrams")

    for i in word_h:
        if word_h[i] > 0:
            print(f"{wordOne} and {wordTwo} are not anagrams")
            return

    print(f"{wordOne} and {wordTwo} are anagrams")

print(check_anagram("silent", "listen"))
print(check_anagram("silent", "listens"))