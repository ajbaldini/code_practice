""" find the missing number in a given integer array of 1 to 100?
"""
import random

def find_missing(numbers, lastNum):
    numMissing = []
    for i in range(1,lastNum+1):
        if i not in numbers:
            numMissing.append(i)
    return numMissing

def build_array(numbers):
    for i in range(1,101):
        numbers.append(i)

def remove_random(numbers, amtRemoved):
    toRemove = []
    for i in range(amtRemoved):
        toRemove = random.randint(1,len(numbers))
        print("Removing: " + str(toRemove))
        numbers.remove(toRemove)
    return numbers

numbers = []
build_array(numbers)
numbers = remove_random(numbers, 4)
missingNums = find_missing(numbers, 100)
print ("missing numbers " + str(missingNums))

