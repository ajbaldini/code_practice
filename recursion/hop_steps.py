"""
count the number of paths a person can take up a set of stairs if they can take one, two or three steps at a time
"""

def hopsteps(n):

    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return hopsteps(n-1) + hopsteps(n-2) + hopsteps(n-3)

print(hopsteps(5))