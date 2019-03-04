"""
replace all spaces with %20
"""

def urlify(s):
    n = ""
    for c in s:
        if c == " ":
            c = "%20"
        n = n + c

    return n

print(urlify("Mr John Smith"))
print(urlify("aa  bb b d"))