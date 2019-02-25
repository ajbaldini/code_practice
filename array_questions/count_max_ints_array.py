"""
Find the biggest ints in an array and count them
"""

def birthdayCakeCandles(ar):
    ar.sort(reverse=True)
    candles = 0
    maxht = ar[0]

    for i in ar:
        if i == maxht:
            candles = candles + 1

    return candles

print(birthdayCakeCandles([3,2,1,3]))