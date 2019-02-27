""" find the missing numbers in a given integer array of 1 to 100?
"""
import random

def build_set(numbers):
    for i in range(1,101):
        numbers.add(i)

def remove_random(numbers):
    toRem = random.randint(1,10)
    for i in range(toRem):
        removeNum = (random.randint(1,100))
        print("Removing: " + str(removeNum))
        numbers.remove(removeNum)
    return numbers

numbers = set()
build_set(numbers)
allnumbers = numbers.copy()
numbers = remove_random(numbers)

d = allnumbers.difference(numbers)

print ("missing number(s) " + str(d))