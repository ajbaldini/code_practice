"""
How do you count the occurrence of a given character in a string
"""

def find_chars(words, target):
    words = words.lower()
    word_cnt = 0
    for i in words:
        if i == target:
            word_cnt = word_cnt + 1
    return word_cnt

words = "The quick brown fox jumped over the lazy dog."
print(str(find_chars(words,'t')))