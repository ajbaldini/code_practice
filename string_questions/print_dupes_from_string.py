"""
How do you print duplicate characters from a string
"""

def print_dupes(test_str):
    checked_chs = []
    dupes = []
    for c in test_str:
        if c in checked_chs:
            dupes.append(c)
        checked_chs.append(c)
    return dupes

test_str = "abccdeefg"
dupes = print_dupes(test_str)
print("Dupes:", " ".join(dupes))

