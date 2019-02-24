"""
How do you count a number of vowels and consonants in a given string?
"""

def count_letters(words):
    vowels = "aeiou"
    consts = "bcdfghjklmnpqrstvwxyz"
    words = words.lower()
    vowels_cnt = 0
    consts_cnt = 0

    for c in words:
        if c in vowels:
            vowels_cnt = vowels_cnt + 1
        elif c in consts:
            consts_cnt = consts_cnt + 1
    return vowels_cnt, consts_cnt


words = "The quick brown fox jumped over the lazy dog."
vowels, consts = count_letters(words)
print(f"vowels {vowels} consts {consts}")