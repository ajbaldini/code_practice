"""
write a function that given a string checks if a palindrome is possible and generates as many permutations as possible
does not have to return sensible words
"""

def isPalindrome(h_left, right_s, middle_c):
    h_left = h_left
    right_s = right_s
    middle_c = middle_c

    for c in right_s:
        if c in h_left:
            h_left[c] -= 1

    v = sorted(h_left.values())
    for i in v:
        if i > 0:
            return print("Palindrome not possible")

    buildPalindrome(h_left,middle_c)

def buildPalindrome(h_left,middle_c):
    h_left = h_left
    middle_c = middle_c
    s = ''

    a_sorted = sorted(h_left.keys())
    a_palin = a_sorted.copy()
    for i in range(len(a_sorted)):
        s = ''.join(a_palin)
        r = s[::-1]
        if middle_c != "":
            s = s + middle_c
        s = s + r

        mv = a_palin.pop(0)
        a_palin.append(mv)

        print(s)

def checkPalindrome(s):
    print(s)
    n = len(s)%2
    h_left = {}
    middle_c = ""
    right_s = ""

    m = int(len(s) / 2)
    if n == 1:
        right_s = s[m + 1:len(s)]
    else:
        right_s = s[m:len(s)]

    middle_c = s[m]
    left_s = s[0:m]

    for c in left_s:
        h_left.setdefault(c,0)
        h_left[c] += 1

    isPalindrome(h_left, right_s, middle_c)

print(checkPalindrome("redder"))
print(checkPalindrome("tacocat"))
print(checkPalindrome("forward"))


